import abc

DOS_EOL = "\r\n"
UNIX_EOL = "\n"


class Source(metaclass=abc.ABCMeta):
    registry = {}

    def __init__(self, text):
        self.text = text
        self.newline = self.discover_newline()

    def __init_subclass__(cls, lang, **kwargs):
        super().__init_subclass__(**kwargs)
        Source.registry[lang] = cls

    def discover_newline(self):
        if DOS_EOL in self.text:
            return DOS_EOL
        else:
            return UNIX_EOL

    def has(self, text):
        return text in self.text

    def first(self, text):
        try:
            return self.text.index(text)
        except ValueError:
            return None

    def end_of_line(self, pos):
        tail = self.the_rest(pos + 1)
        npos = tail.first(self.newline)
        if npos:
            return pos + 1 + npos
        return 0

    def the_rest(self, pos):
        return self.__class__(self.text[pos:])

    @abc.abstractmethod
    def find_insert_pos(self):
        pass

    @abc.abstractmethod
    def fix_import_text(self, text):
        pass

    def add_import(self, primary_text, *, secondary_text=None):
        text = self.text
        pos = self.find_insert_pos()
        newline = self.newline

        fixed = self.fix_import_text(primary_text, secondary_text=secondary_text)
        res = text[:pos] + newline + fixed + newline + text[pos:]
        return res


# Note:
# must be *after* the Source class to avoid circular imports
# we must import the modules so that the __init_subclass__ hook
# is called

from .c import CSource, CPPSource
from .javascript import JavaScriptSource
from .python import PythonSource

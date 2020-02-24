from .c_source import CSource
from .python_source import PythonSource


class Adder:
    def __init__(self, source_text, *, lang):
        self.lang = lang
        if lang in ("c", "cpp"):
            self.source = CSource(source_text)
        else:
            self.source = PythonSource(source_text)

    def add_import(self, import_text):
        return self.source.add_import(import_text)

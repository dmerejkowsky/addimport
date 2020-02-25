from .source import Source

IFDEF = "#ifdef"
IFNDEF = "#ifndef"
INCL = "#include"


class CSource(Source):
    def __init__(self, text):
        super().__init__(text)

        self._has_ifdef = self.has(IFDEF)
        self._has_ifndef = self.has(IFNDEF)
        self._has_include = self.has(INCL)

    def fix_import_text(self, primary_text, *, secondary_text=None):
        if primary_text.startswith("#include"):
            return primary_text
        else:
            return "#include " + primary_text

    def has_ifdef(self):
        return self._has_ifdef

    def has_ifndef(self):
        return self._has_ifndef

    def has_include(self):
        return self._has_include

    def first_ifdef(self):
        return self.first(IFDEF)

    def first_ifndef(self):
        return self.first(IFNDEF)

    def first_include(self):
        return self.first(INCL)

    def first_include_after_ifdef(self):
        return self.first_include_after_word(IFDEF)

    def first_include_after_ifndef(self):
        return self.first_include_after_word(IFNDEF)

    def has_ifdef_before(self, pos):
        found = self.first_ifdef()
        return found and (found < pos)

    def first_include_after_word(self, word):
        if not self.has_include() and not self.has(word):
            return 0
        if self.has_include() and not self.has(word):
            return self.first_include()

        pos = self.first(word)
        tail = self.the_rest(pos)
        if tail.has_include():
            return pos + tail.first_include()
        return pos

    def find_insert_pos(self):  # noqa: C901
        has_include = 1
        has_ifdef = 2
        has_ifndef = 4

        n = 0
        if self.has_include():
            n |= has_include

        if self.has_ifdef():
            n |= has_ifdef

        if self.has_ifndef():
            n |= has_ifndef

        pos = 0

        if n == has_include:
            pos = self.first_include()
        elif n == has_ifdef:
            pos = self.first_ifdef()
        elif n == has_ifndef:
            pos = self.first_ifndef()
        elif n == has_ifdef | has_ifndef:
            pos = min(self.first_ifdef(), self.first_ifndef())
        elif n == has_include | has_ifdef:
            pos = self.first_include_after_ifdef()
        elif n == has_include | has_ifndef:
            pos = self.first_include_after_ifndef()
        elif n == has_include | has_ifndef | has_ifndef:
            pos = min(
                self.first_include_after_ifdef(), self.first_include_after_ifndef()
            )
        else:
            return 0

        return self.end_of_line(pos)

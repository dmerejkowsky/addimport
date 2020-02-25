from .source import Source


class PythonSource(Source):
    def __init__(self, text):
        self.text = text
        self.newline = self.discover_newline()

    def find_insert_pos(self):
        pos = self.first("import")
        return self.end_of_line(pos)

    def fix_import_text(self, s):
        if "import" in s:
            return s
        n_words = len(s.split())
        if n_words == 2:
            x, y = s.split()
            return f"from {y} import {y}"
        else:
            return f"import {s}"

from .source import Source


class PythonSource(Source):
    def __init__(self, text):
        self.text = text
        self.newline = self.discover_newline()

    def find_insert_pos(self):
        pos = self.first("import")
        return self.end_of_line(pos)

    def fix_import_text(self, primary_text, *, secondary_text=None):
        if "import" in primary_text:
            return primary_text

        if secondary_text:
            return f"from {primary_text} import {secondary_text}"
        else:
            return f"import {primary_text}"

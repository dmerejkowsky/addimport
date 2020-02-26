from .source import Source


class JavaScriptSource(Source, lang="javascript"):
    def __init__(self, text):
        self.text = text
        self.newline = self.discover_newline()
        self.use_require = False

    def find_insert_pos(self):
        n1 = self.first("import ")
        n2 = self.first("require(")
        if n1 and n2:
            return self.end_of_line(min(n1, n2))
        if n1 and not n2:
            return self.end_of_line(n1)
        if n2 and not n1:
            self.use_require = True
            return self.end_of_line(n2)
        return 0

    def fix_import_text(self, primary_text, *, secondary_text=None):
        if self.use_require:
            return f"const {primary_text} = require('{secondary_text}');"
        else:
            return f"import {{ {primary_text} }} from {secondary_text};"

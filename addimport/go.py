from .source import Source


class GoSource(Source, lang="go"):
    def __init__(self, text):
        super().__init__(text)

    def find_insert_pos(self):
        pos = self.first("import")
        if not pos:
            return 0
        n = self.end_of_line(pos)
        if not n:
            return 0
        the_rest = self.the_rest(n)
        first_import = the_rest.first('"')
        if not first_import:
            return self.end_of_line(n)
        res = n + first_import
        return self.end_of_line(res)

    def fix_import_text(self, primary_text, *, secondary_text=None):
        return f'\t"{primary_text}"'

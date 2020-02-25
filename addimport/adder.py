from .source import Source


class Adder:
    def __init__(self, source_text, *, lang):
        self.lang = lang
        cls = Source.registry.get(lang)
        if not cls:
            raise NotImplementedError(f"unsupported lang: {lang}")
        self.source = cls(source_text)

    def add_import(self, primary_text, *, secondary_text=None):
        return self.source.add_import(primary_text, secondary_text=secondary_text)

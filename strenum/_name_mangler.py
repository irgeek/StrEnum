import re


class _NameMangler:
    _regex = re.compile(r"([A-Z]?[a-z]+)|([A-Z]+(?![a-z]))")

    def words(self, name):
        """
        Split a string into words. Should correctly handle splitting:
            camelCase
            PascalCase
            kebab-case
            snake-case
        """
        yield from (m.group(0) for m in self._regex.finditer(name))

    def camel(self, name):
        """
        Convert a name to camelCase
        """

        def cased_words(word_iter):
            yield next(word_iter, "").lower()
            yield from (w.title() for w in word_iter)

        return "".join(cased_words(self.words(name)))

    def pascal(self, name):
        """
        Convert a name to PascalCase
        """

        return "".join(w.title() for w in self.words(name))

    def kebab(self, name):
        """
        Convert a name to kebab-case
        """

        return "-".join(w.lower() for w in self.words(name))

    def snake(self, name):
        """
        Convert a name to snake_case
        """

        return "_".join(w.lower() for w in self.words(name))

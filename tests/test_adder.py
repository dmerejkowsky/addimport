import textwrap

from addimports import Adder


def test_adder():
    """ Can add a missing import to a Python file """

    source = textwrap.dedent(
        """\
        #!/bin/env python3

        import sys

        def main():
            pass

        """
    )
    adder = Adder(lang="python", source=source)
    new_source = adder.add_import("os")
    assert new_source == textwrap.dedent(
        """\
        #!/bin/env python3

        import os
        import sys

        def main():
            pass

        """
    )

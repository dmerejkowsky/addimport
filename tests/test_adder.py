import textwrap
import pytest

from addimports import Adder


def test_c_adder():
    buffer = textwrap.dedent(
        """\
        #ifndef _FOO_H
        #define _FOO_H

        #include <foo.h>

        #endif
        """
    )
    adder = Adder(buffer, lang="c")
    actual = adder.add_import("<bar.h>")
    expected = textwrap.dedent(
        """\
        #ifndef _FOO_H
        #define _FOO_H

        #include <foo.h>
        #include <bar.h>


        #endif
        """
    )
    assert actual == expected


@pytest.mark.skip("not ready")
def test_python_adder():
    """ Can add a missing import to a Python file """

    buffer = textwrap.dedent(
        """\
        #!/bin/env python3

        import sys

        def main():
            pass

        """
    )
    adder = Adder(buffer, lang="python")
    buffer = adder.add_import("os")
    assert buffer == textwrap.dedent(
        """\
        #!/bin/env python3

        import os
        import sys

        def main():
            pass

        """
    ), buffer

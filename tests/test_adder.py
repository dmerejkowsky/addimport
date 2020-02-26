import textwrap
import pytest

from addimport.adder import Adder


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
    actual = adder.add_import("<bar.h>", secondary_text=None)
    # Note the added blank line after bar.h,
    # it's a bug from the original implem  ¯\_(ツ)_/¯
    expected = textwrap.dedent(
        """\
        #ifndef _FOO_H
        #define _FOO_H

        #include <foo.h>
        #include <bar.h>


        #endif
        """
    )
    assert repr(actual) == repr(expected)


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
    actual = adder.add_import("os", secondary_text=None)
    expected = textwrap.dedent(
        """\
        #!/bin/env python3

        import sys
        import os


        def main():
            pass

        """
    )
    assert repr(actual) == repr(expected)


def test_javascript_adder_requires():
    """ Can add a missing require() call to a JavaScript file """
    buffer = textwrap.dedent(
        """\
        const foo = require('foo');

        module.exports = baz;
        """
    )
    adder = Adder(buffer, lang="javascript")
    actual = adder.add_import("bar", secondary_text="bar")
    expected = textwrap.dedent(
        """\
        const foo = require('foo');
        const bar = require('bar');


        module.exports = baz;
        """
    )
    assert repr(actual) == repr(expected)

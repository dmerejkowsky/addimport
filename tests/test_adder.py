import textwrap
import pytest

from addimports.adder import Adder, CSource, fix_include


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


def test1():
    testcontent = """#ifdef SOMETHING

#include <blubbelubb.h>

#define SOMETHING
#endif /* SOMETHING */
"""
    source = CSource(testcontent)
    assert source.find_insert_pos() == 41


def test2():
    testcontent = '#include "paraply.h"\n'
    source = CSource(testcontent)
    assert source.find_insert_pos() == 20


def test3():
    testcontent = """#ifdef SOMETHING
#define SOMETHING
#endif"""
    source = CSource(testcontent)
    assert source.find_insert_pos() == 16


def test4():
    testcontent = ""
    source = CSource(testcontent)
    assert source.find_insert_pos() == 0


def test5():
    testcontent = """#include "jeje.h"

#ifdef SOMETHING

#include "ostebolle.h"

#endif"""
    source = CSource(testcontent)
    assert source.find_insert_pos() == 59


def test6():
    testcontent = """#include "jeje.h"

#ifdef SOMETHING

#include "ostebolle.h"
#include <stdlib.h>


#endif"""
    source = CSource(testcontent)
    assert source.find_insert_pos() == 59


def test_fix_include():
    """ It should add #include if it's missing """
    assert fix_include('"foo.h"') == '#include "foo.h"'
    assert fix_include("#include <bar>") == "#include <bar>"

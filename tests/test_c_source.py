from addimport.c_source import CSource


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
    source = CSource("")
    assert source.fix_import_text('"foo.h"', secondary_text=None) == '#include "foo.h"'
    assert (
        source.fix_import_text("#include <bar>", secondary_text=None)
        == "#include <bar>"
    )

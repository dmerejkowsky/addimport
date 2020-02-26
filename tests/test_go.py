from addimport.go import GoSource


def test1():
    testcontent = """package foo

import (
  "github.com/foo/bar"
)

func main() {
}
"""
    source = GoSource(testcontent)
    assert source.find_insert_pos() == 44

from addimport.python import PythonSource


def test1():
    testcontent = """#!/bin/python
''' the doc string '''

import os

def main():
    ...
"""
    source = PythonSource(testcontent)
    assert source.find_insert_pos() == 47

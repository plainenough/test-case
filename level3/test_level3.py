#!/usr/bin/env python3
import pytest

userlist = ['dwalton', 'kgibson', 'adelacruz',
            'dpfister', 'ohuweih']


@pytest.mark.parametrize("filename", userlist)
def test_original(filename):
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert original == 'Hello world', "Test failed"


@pytest.mark.parametrize("filename", userlist)
def test_upper(filename):
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert upper == 'HELLO WORLD', "Test failed"


@pytest.mark.parametrize("filename", userlist)
def test_lower(filename):
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert lower == 'hello world', "Test failed"


@pytest.mark.parametrize("filename", userlist)
def test_endup(filename):
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert endup == 'hellO worlD', "Test failed"


@pytest.mark.parametrize("filename", userlist)
def test_begup(filename):
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert begup == 'Hello World', "Test failed"

#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize(
        "filename",
        ['dwalton',
         'kgibson',
         'adelacruz',
         'ohuweih'])
def test_original(filename):
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert original == 'Hello world', "Test failed"


@pytest.mark.parametrize(
        "filename",
        ['dwalton',
         'kgibson',
         'adelacruz',
         'ohuweih'])
def test_upper(filename):
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert upper == 'HELLO WORLD', "Test failed"


@pytest.mark.parametrize(
        "filename",
        ['dwalton',
         'kgibson',
         'adelacruz',
         'ohuweih'])
def test_lower(filename):
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert lower == 'hello world', "Test failed"


@pytest.mark.parametrize(
        "filename",
        ['dwalton',
         'kgibson',
         'adelacruz',
         'ohuweih'])
def test_endup(filename):
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert endup == 'hellO worlD', "Test failed"


@pytest.mark.parametrize(
        "filename",
        ['dwalton',
         'kgibson',
         'adelacruz',
         'ohuweih'])
def test_begup(filename):
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert begup == 'Hello World', "Test failed"

#!/usr/bin/env python3
import pytest

userlist = ['dwalton', 'kgibson', 'adelacruz',
            'dpfister', 'ohuweih', 'jearl',
            'mflederbach', 'ktilley']


@pytest.mark.parametrize("filename", userlist)
def test_original(filename):
    ''' This test validates: 'Hello world'
    '''
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert original == 'Hello world', "Test failed"


@pytest.mark.parametrize("filename", userlist)
def test_upper(filename):
    ''' This test validates: 'HELLO WORLD'
    '''
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert upper == 'HELLO WORLD', "Test failed"


@pytest.mark.parametrize("filename", userlist)
def test_lower(filename):
    ''' This test validates: 'hello world'
    '''
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert lower == 'hello world', "Test failed"


@pytest.mark.parametrize("filename", userlist)
def test_endup(filename):
    ''' This test validates: 'hellO worlD'
    '''
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert endup == 'hellO worlD', "Test failed"


@pytest.mark.parametrize("filename", userlist)
def test_begup(filename):
    ''' This test validates: 'Hello World'
    '''
    myfile = __import__(filename)
    (original, upper, lower, endup, begup) = myfile.main()
    assert begup == 'Hello World', "Test failed"

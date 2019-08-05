#!/usr/bin/env python3
import pytest

def test_original(import_testing):
    ''' This test validates: 'Hello world'
    '''
    dictionary = import_testing("oriGinal")
    assert dictionary['input'] == 'oriGinal', "Test failed"

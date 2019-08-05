#!/usr/bin/env python3
import pytest
import os
#userlist = ['dwalton', 'kgibson', 'adelacruz',
#            'dpfister', 'ohuweih', 'jearl',
#            'mflederbach', 'ktilley']


@pytest.fixture()
def import_testing():
    ''' This setup will take care of loading the desired file.
    '''
    HERE = os.getcwd()
    import __main__ as program
    testfile = program.main()
    return testfile

#!/usr/bin/env python3


def args():
    '''This function just loads the argmunts by default the assumption
    is made that the target template exists in the programs working
    directory
    '''
    import argparse
    parser = argparse.ArgumentParser(description='Test 1')
    parser.add_argument("filename", help='Example: Joe schmoe -> jschmoe',
                        type=str)
    return parser.parse_args()


def loadFile(filename):
    '''This will load the values from the target code for test setup
    '''
    myResult = __import__(filename)
    (regular, upper, lower) =  myResult.main()    
    return regular, upper, lower


def testReg(test1):
    '''This test will validate the intended format "Hello world"
    '''
    if test1 == 'Hello world':
        return True
    else:
        return False


def testUpper(test2):
    '''This test will ensure all characters are upper case
    '''
    if test2 == 'HELLO WORLD':
        return True
    else:
        return False


def testLower(test3):
    '''This test will ensure all characters are lower case
    '''
    if test3 == 'hello world':
        return True
    else:
        return False


if __name__ == '__main__':
    args = args()
    count = 0
    results = {}
    (test1, test2, test3) = loadFile(args.filename)
    for mytest in testReg(test1), testUpper(test2), testLower(test3):
        count += 1 
        results["test{0}".format(count)] = mytest
    for test in results:
        print("{0} - {1}".format(test, results[test]))

#!/usr/bin/env python3


def loadFile(filename):
    myResult = __import__(filename)
    if myResult.main() == 'Hello world':
        return True
    else:
        return False


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


if __name__ == '__main__':
    args = args()
    result = loadFile(args.filename)
    if result:
        print("Test passed")
    else:
        print("Test Failed")

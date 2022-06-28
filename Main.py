import argparse
from Driver import Driver

class Main:
    def __init__(self, args):
        self.driver = Driver(args)
        self.driver.start_execution()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-op', '--operation', choices=['encode', 'decode'], required=True)
    parser.add_argument('-i', '--input', required=True, help='path of input file')
    parser.add_argument('-o', '--output', required=True, help='path of output file (must be nonexistent)')
    parser.add_argument('-b64', '--use-base64', action='store_true', help='if this argument is used:\n' +
        '\t- In encode operation, firstly, the input data is encoded using base64, then it is encoded to image.\n' + 
        '\t- In decode operation, the data derived from encoded image is decoded using base64.\n' + 
        '\t  This option should be used in decode operation only if the image to be decoded was created by using -b64 argument.\n' + 
        'Usage of -b64 is useful when input data includes unicode characters since the encoding process supports only ASCII characters.\n' + 
        'Also, encode and decode operations for binary files must be done with -b64 option enabled.')
    main = Main(args = parser.parse_args())

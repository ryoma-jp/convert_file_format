
import argparse
from lib.svg2png import svg2png

SUPPORT_CONVERT = [
    'svg2png',
]

def arg_parser():
    """Argument Parser
    
    Parsing arguments
    
    Returns:
        - arguments of Namespace object
    """
    parser = argparse.ArgumentParser(description='Convert file format',
                formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('--convert_type', dest='convert_type', type=str, choices=SUPPORT_CONVERT, required=True, \
            help='convert type')

    parser.add_argument('--input_file', dest='input_file', type=str, required=True, \
            help='input file path')
    parser.add_argument('--output_file', dest='output_file', type=str, required=True, \
            help='output file path')
    
    args = parser.parse_args()

    return args
    
def main():
    """main
    
    Main function
    """
    args = arg_parser()
    print(f'convert_type: {args.convert_type}')
    print(f'input_file: {args.input_file}')
    print(f'output_file: {args.output_file}')
    
    if (args.convert_type == 'svg2png'):
        svg2png(args.input_file, args.output_file)
    else:
        print(f'{args.convert_type} is NOT supported')
    
if __name__=='__main__':
    main()




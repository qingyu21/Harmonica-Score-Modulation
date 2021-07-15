# import pyparsing
import argparse
import sys

pitches=['C','Cb','D','Db','E','F','Gb','G','Ab','A','Bb','B']
# numberToPitch={'C':}

input_key='C'
output_key='C'
input_file=''
pitch_interval=0

def get_input_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i","--input",help="input key",type=str)
    parser.add_argument("-o","--output",help="output key",type=str)
    parser.add_argument("-f","--file",help="input file",type=str)

    args=parser.parse_args()

    global input_key,output_key,input_file

    input_key=args.input
    output_key=args.output
    input_file=args.file

def parse_line():
    pass

def parse_input():
    f=open(input_file,'r')
    for line in f.readlines():
        print(line,end="")


def modulation():
    # get input
    get_input_arguments()

    # parse input
    parse_input()

    # modulation
    


if __name__ == "__main__":
    modulation()


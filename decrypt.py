from interpolation import interpolate
import sys

def parse_input():
    input_pairs = [x.split(":") for x in sys.argv[1:]]
    input_pairs = [x for x in input_pairs if len(x) == 2]
    input_pairs = [(int(x), int(y)) for x, y in input_pairs if x.isdigit() and y.isdigit()]
    print("Input: ", input_pairs, "\n\n")
    input_x = [x for x, y in input_pairs]
    input_y = [y for x, y in input_pairs]
    return input_x, input_y

########################################################

q = (13 ** 5)

input_x, input_y = parse_input()
recovered_secret = interpolate(0, input_x, input_y, q)


#######################################################
print("Common secret: ", recovered_secret)

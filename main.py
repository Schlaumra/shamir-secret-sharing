import random
import secrets
from interpolation import interpolate, eval_poly
from tools import format_poly, print_keys, print_hidden_step, print_step

# q = p^r p is a prime and r is a positive integer
# defines our finite field Z_q
q = (13 ** 5) # Should be a big prime number to create a finite field

print("\n\n#################### INPUT #######################")


n_keys = int(input("Number of keys: "))
n_req_keys = int(input("Number of required keys: "))
# This is the secret we want to share between the keys
common_secret = int(input("Secret: "))

# Assert correctness
assert n_keys >= n_req_keys, "Wrong input"
assert n_keys > 0
assert n_req_keys > 0
assert common_secret < q


print("\n\n#################### CREATE #######################")

print_step(1, f"Use {q} for finite field")

# Random chosen n_req_keys-1: [secret, rnd1, rnd2, rnd3]
coefficients = []
while len(coefficients) < n_req_keys-1:
    tmp = secrets.randbelow(q-1)
    if tmp not in coefficients:
        coefficients.append(tmp)
secret_poly = [
    common_secret,
    *coefficients
]
print_hidden_step(2, f"Random coefficients: ", coefficients)

# Never do this: It should be kept secret at all costs
print_hidden_step(3, f"Created polynomial: ", format_poly(secret_poly))

# Create items of form (x, y) for the first 
keys = [(i+1, eval_poly(secret_poly, i+1, q)) for i in range(n_keys)]

print_step(4, f"Calculate f(x) for x{list(range(1, n_keys+1))}\n")
print_step(5, "Distribute values separately to end users:", "\n")
print_keys(keys)


print("\n\n#################### DECRYPT #######################")
    
def get_random_input_keys():
    input_keys = []
    while(len(input_keys) < n_req_keys):
        i = random.randint(0, n_keys-1)
        if(keys[i] not in input_keys):
            input_keys.append(keys[i])
    return input_keys

print_step(1, "Let each end user input their own key")
input_keys = get_random_input_keys()
print_step(2, "Users entered: ", input_keys)
input_x = [x for x, y in input_keys]
input_y = [y for x, y in input_keys]


recovered_secret = interpolate(0, input_x, input_y, q)

print("recovered_secret", recovered_secret)

############################################

import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

plt.scatter(range(1, n_keys+1), [x for (_, x) in keys], label='keys')
plt.scatter(input_x, input_y, label='input_keys')

poly_x = np.arange(-1, n_keys+10, step=0.01)
plt.scatter(poly_x, eval_poly(secret_poly, poly_x, q), label='f(x)', s=2)

plt.legend()
plt.show()

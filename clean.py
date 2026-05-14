import random
import secrets
from interpolation import interpolate, eval_poly
from tools import format_poly, print_keys, print_hidden_step, print_step

# q = p^r p is a prime and r is a positive integer
# defines our finite field Z_q
q = (13 ** 5) # Should be a big prime number to create a finite field

# Random coeff smaller n_req_keys-1: [secret, rnd1, rnd2, rnd3]
coefficients = ...
secret_poly = [
    common_secret,
    *coefficients
]

# Create for every x position [1,n_keys+1] a shared secret f(x) modulo q
for i in range(1, n_keys+1):
    print(f"{i}: {eval_poly(secret_poly, i, q)}")


############################## Decrypt

# input_x=[1,   2,   3,   4  ]    x
# input_y=[123, 511, 123, 155]  f(x)
input_x, input_y = ...
# Calculate f(0) to get the secret use interpolation to do this (moulo q)
recovered_secret = interpolate(0, input_x, input_y, q)

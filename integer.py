import numpy as np
from scipy.interpolate import lagrange
import secrets

number_of_keys = 6
number_of_required_keys = 3

keys_coeff = [secrets.randbelow(10000000) for x in range(number_of_required_keys-1)] # Random chosen number_of_required_keys-1
common_secret = 1234 # This is the secret we want to share between the keys
secret_poly = np.poly1d([*keys_coeff, common_secret])

print(keys_coeff)
keys = [(i+1, secret_poly(i+1)) for i in range(number_of_keys)]

for i, x in keys:
    print(f"Secret {i+1}: {x}")


input_keys = [x for x in keys[-number_of_required_keys-1:-1]]
print(input_keys)
input_x = [x for x, y in input_keys]
input_y = [y for x, y in input_keys]
recv_poly = lagrange(input_x, input_y)


print(recv_poly)
recovered_secret = int(recv_poly.c[-1])


print("secret", recovered_secret)



import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

plt.scatter(range(1, number_of_keys+1), [x for (_, x) in keys], label='keys')
plt.scatter(input_x, input_y, label='input_keys')
poly_x = np.arange(-10, number_of_keys+10, step=0.1)
plt.plot(poly_x, secret_poly(poly_x), label='Secret poly')
plt.legend()
plt.show()

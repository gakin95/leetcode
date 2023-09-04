import numpy as np


def reverse(x: int) -> int:
    y = str(abs(x))
    z = []
    for char in reversed(y):
        z.append(char)
    print(z)
    return np.sign(x) * int("".join(z))

print(reverse(123))
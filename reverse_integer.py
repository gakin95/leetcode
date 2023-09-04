class Solution:
    def reverse(self, x: int) -> int:
        y = str(abs(x))
        z = []
        w = 1
        if x < 0:
            w = -1
        for char in reversed(y):
            z.append(char)

        reversed_int = w * int("".join(z))

        if reversed_int < -2 ** 31 or reversed_int > 2 ** 31 - 1:
            return 0

        return reversed_int

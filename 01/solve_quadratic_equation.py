from sys import stdin
from math import sqrt, isclose


def solve_square(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    denominator = 0.5 / a

    if isclose(discriminant, 0):
        x_1 = -b * denominator
        return x_1,

    if discriminant > 0:
        sqrt_d = sqrt(discriminant)
        x_1 = (-b - sqrt_d) * denominator
        x_2 = (-b + sqrt_d) * denominator
        return x_1, x_2


def main():
    assert solve_square(2, 1, 5) is None
    res = solve_square(1, -2, 1)
    assert len(res) == 1 and isclose(res[0], 1)
    res = solve_square(1, -0.5, -3)
    assert len(res) == 2 and isclose(res[0], -1.5) and isclose(res[1], 2)

    a, b, c = map(float, input().split())
    if isclose(a, 0):
        print("x^2 coefficient should not be zero")
    else:
        print(solve_square(a, b, c))


if __name__ == '__main__':
    main()

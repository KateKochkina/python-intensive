from sys import stdin
from math import sqrt

EPS = 1e-10


def solve_square(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    denominator = 0.5 / a

    if abs(discriminant) < EPS:
        x_1 = -b * denominator
        return x_1,

    if discriminant > 0:
        sqrt_d = sqrt(discriminant)
        x_1 = (-b - sqrt_d) * denominator
        x_2 = (-b + sqrt_d) * denominator
        return x_1, x_2


def main():
    assert solve_square(2, 1, 5) is None
    assert solve_square(1, -2, 1) == (1.0, )
    assert solve_square(1, -0.5, -3) == (-1.5, 2.0)

    a, b, c = map(float, input().split())
    if abs(a) < EPS:
        print("x^2 coefficient should not be zero")
    else:
        print(solve_square(a, b, c))


if __name__ == '__main__':
    main()

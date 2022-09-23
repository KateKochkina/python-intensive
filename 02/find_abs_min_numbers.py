import sys


def find_abs_min_numbers(arr):
    val_min_abs = float('inf')
    res = []
    for x in arr:
        x_abs = abs(x)
        if x_abs < val_min_abs:
            val_min_abs = x_abs
            res = [x]
        elif x_abs == val_min_abs:
            res.append(x)
    return res


def main():
    assert find_abs_min_numbers([3, 2, 1, 0, -1]) == [0]
    assert find_abs_min_numbers([-5, 9, 6, -8]) == [-5]
    assert find_abs_min_numbers([-1, 2, -5, 1, -1]) == [-1, 1, -1]

    arr = list(map(int, sys.stdin.readline().split()))
    print(find_abs_min_numbers(arr))


if __name__ == '__main__':
    main()

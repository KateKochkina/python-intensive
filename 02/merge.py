import sys


def merge(arr_1, arr_2):
    i_1, i_2 = 0, 0
    res = set()
    while i_1 < len(arr_1) and i_2 < len(arr_2):
        if arr_1[i_1] < arr_2[i_2]:
            i_1 += 1
        elif arr_1[i_1] > arr_2[i_2]:
            i_2 += 1
        else:
            res.add(arr_1[i_1])
            i_1 += 1
            i_2 += 1
    return list(res)


def main():
    assert merge([1, 1, 2, 5, 7], [1, 1, 2, 3, 4, 7]) == [1, 2, 7]
    assert merge([-5, -1, 0, 5, 7], [-8, -5, 2, 3, 4, 7]) == [-5, 7]

    arr_1 = list(map(int, sys.stdin.readline().split()))
    arr_2 = list(map(int, sys.stdin.readline().split()))
    print(merge(arr_1, arr_2))


if __name__ == '__main__':
    main()

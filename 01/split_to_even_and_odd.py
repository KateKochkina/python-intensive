from sys import stdin


def even_odd_numbers(arr):
    even = []
    odd = []

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])

    return even, odd


def main():
    assert even_odd_numbers([1, 2, 3, 4, 5, 6, 7]) == ([2, 4, 6], [1, 3, 5, 7])
    assert even_odd_numbers([1, 8, 3, 4, 5, 6, 7, 16, 19]) == ([8, 4, 6, 16], [1, 3, 5, 7, 19])

    arr = list(map(int, stdin.readline().split()))
    ans = even_odd_numbers(arr)
    print(ans)


if __name__ == '__main__':
    main()

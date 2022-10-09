from custom_list import CustomList

lst1, lst2 = CustomList([5, 5, 5]), CustomList([1, 1, 1])
assert list(lst1 - lst2) == [4, 4, 4]
assert list(lst2 - lst1) == [-4, -4, -4]

lst1, lst2 = CustomList([3, 3]), CustomList([1, 1, 1])
assert list(lst1 - lst2) == [2, 2, -1]
assert list(lst2 - lst1) == [-2, -2, 1]

lst3 = CustomList([2, 2, 2])
assert list(lst3 - lst2 - lst1) == [-2, -2, 1]

lst1, lst2 = CustomList([6, 6, 6]), CustomList([1, 1, 1])
assert list(lst1 + lst2) == [7, 7, 7]
assert list(lst2 + lst1) == [7, 7, 7]

lst1, lst2 = CustomList([3, 3]), CustomList([1, 1, 1])
assert list(lst1 + lst2) == [4, 4, 1]
assert list(lst2 + lst1) == [4, 4, 1]

lst3 = CustomList([5, 5, 5])
assert list(lst3 + lst2 + lst1) == [9, 9, 6]

lst1, lst2 = CustomList([1, 1, 1]), [1, 1, 1]
assert list(lst1 + lst2) == [2, 2, 2]
assert list(lst2 + lst1) == [2, 2, 2]
assert list(lst1 - lst2) == [0, 0, 0]
assert list(lst2 - lst1) == [0, 0, 0]

lst1, lst2 = [8, 8], CustomList([1, 1, 1])
assert list(lst1 + lst2) == [9, 9, 1]
assert list(lst2 + lst1) == [9, 9, 1]
assert list(lst1 - lst2) == [7, 7, -1]
assert list(lst2 - lst1) == [-7, -7, 1]

lst3 = CustomList([4, 4, 4])
assert list(lst3 + lst2 + lst1) == [13, 13, 5]
assert list(lst3 - lst2 - lst1) == [-5, -5, 3]

lst1, lst2 = CustomList([4, 4]), CustomList([1, 1, 1])
lst3 = lst1 + lst2
assert len(lst3) == 3 and len(lst1) == 2 and len(lst2) == 3

lst3 = lst1 - lst2
assert len(lst3) == 3 and len(lst1) == 2 and len(lst2) == 3

lst1, lst2 = CustomList([2, 2]), CustomList([1, 1, 1])
assert (lst1 == lst2) is False
assert (lst1 != lst2) is True
assert (lst1 > lst2) is True
assert (lst1 < lst2) is False
assert (lst1 >= lst2) is True
assert (lst1 <= lst2) is False

lst1, lst2 = CustomList([7, 3]), CustomList([3, 3, 4])
assert (lst1 == lst2) is True
assert (lst1 != lst2) is False
assert (lst1 > lst2) is False
assert (lst1 < lst2) is False
assert (lst1 >= lst2) is True
assert (lst1 <= lst2) is True

print(lst1)

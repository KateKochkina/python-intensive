from itertools import zip_longest


class CustomList(list):

    def get_elem_or_zero(self, index):
        if index < len(self):
            return self[index]
        else:
            return 0

    def __add__(self, other):
        if not isinstance(other, list):
            raise TypeError("The right operand must be a list")

        sum_lst = [sum(x) for x in zip_longest(self, other, fillvalue=0)]
        return CustomList(sum_lst)

    def __radd__(self, other):
        if not isinstance(other, list):
            raise TypeError("The right operand must be a list")

        return self + CustomList(other)

    @classmethod
    def neg(cls, lst):
        return cls([-x for x in lst])

    def __sub__(self, other):
        if not isinstance(other, list):
            raise TypeError("The right operand must be a list")

        return self + CustomList.neg(other)

    def __rsub__(self, other):
        if not isinstance(other, list):
            raise TypeError("The right operand must be a list")

        return CustomList.neg(self) + other

    def __eq__(self, other):
        if not isinstance(other, (list, CustomList)):
            raise TypeError("The operand on the right must have values list or CustomList")
        return sum(self) == sum(other)

    def __ne__(self, other):
        if not isinstance(other, (list, CustomList)):
            raise TypeError("The operand on the right must have values list or CustomList")
        return sum(self) != sum(other)

    def __lt__(self, other):
        if not isinstance(other, (list, CustomList)):
            raise TypeError("The operand on the right must have values list or CustomList")
        return sum(self) < sum(other)

    def __le__(self, other):
        if not isinstance(other, (list, CustomList)):
            raise TypeError("The operand on the right must have values list or CustomList")
        return sum(self) <= sum(other)

    def __gt__(self, other):
        if not isinstance(other, (list, CustomList)):
            raise TypeError("The operand on the right must have values list or CustomList")
        return sum(self) > sum(other)

    def __ge__(self, other):
        if not isinstance(other, (list, CustomList)):
            raise TypeError("The operand on the right must have values list or CustomList")
        return sum(self) >= sum(other)

    def __str__(self):
        return f'CustomList elements = {list(self)}\tCustomList sum = {sum(self)}'

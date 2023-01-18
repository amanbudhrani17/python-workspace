import functools
from random import *


def problem1(str: str) -> list:
    """function to break down a string into a list of characters.
    doctests:
    >>> problem1("abcd")
    ['a', 'b', 'c', 'd']
    >>> problem1("abc")
    ['a', 'b', 'c']
    """
    List = list()
    for c in str:
        List.append(c)
    return List


def problem2(List: list) -> str:
    """a function to reverse output of the problem 1 back into a string
    doctests:
    >>> problem2(['a', 'b', 'c', 'd'])
    'abcd'
    >>> problem2(['a', 'b', 'c'])
    'abc'

    """
    str = ""
    for i in List:
        str += i
    return str


def problem3(a: int) -> list:
    """a function generate a list of n random numbers.
    doctests:
    >>> res = problem3(5)
    >>> all([0 <= val <= 5 for val in res])
    True
    >>> res = problem3(3)
    >>> all([0 <= val <= 3 for val in res])
    True
    """
    List = list()
    for i in range(a):
        List.append(randint(0, a))
    return List


def problem4(arr: list) -> list:
    """a function to sort a given list of numbers in descending order.
    doctests:
    >>> problem4([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    >>> problem4([6, 9, 12, 5, 4])
    [12, 9, 6, 5, 4]
    """

    List = list()
    for i in arr:
        a = len(List)
        binaryAdd(0, len(List) - 1, i, List)
        if a == len(List):
            List.append(i)
    return List[::-1]


def binaryAdd(low: int, high: int, a: int, myList: list):
    if low > high:
        return
    mid = int((low + high) / 2)
    if mid == high or (myList[mid] >= a and (mid - 1 < 0 or myList[mid - 1] <= a)):
        if mid == high:
            if a > myList[high]:
                myList.append(a)
            else:
                myList.insert(mid, a)
        else:
            myList.insert(mid, a)
    elif myList[mid] < a:
        binaryAdd(mid + 1, high, a, myList)
    else:
        binaryAdd(low, mid - 1, a, myList)


def problem5(List: list) -> dict:
    """a function to get frequency of each numbers in a list of numbers.
    doctests:
    >>> problem5([1, 1, 3, 2, 3, 2, 3, 2, 2])
    {1: 2, 3: 3, 2: 4}
    >>> problem5([6, 9, 6, 9, 6])
    {6: 3, 9: 2}
    """

    d = dict()
    for i in List:
        if i in d.keys():
            d[i] = d.get(i) + 1
        else:
            d[i] = 1
    return d


def problem6(List: list) -> set:
    """a function to get all the unique elements from given list.
    doctests:
    >>> problem6([1, 1, 3, 2, 3, 2, 3, 2, 2])
    {1, 2, 3}
    >>> problem6([6, 9, 6, 9, 6])
    {9, 6}
    """
    s = set()
    for i in List:
        s.add(i)
    return s


def problem7(List: list) -> int:
    """a function to get the first repeating element from list.
    doctests:
    >>> problem7([1, 2, 3, 4, 5, 1, 2])
    1
    >>> problem7([6, 8, 5, 8, 4])
    8
    """

    s = set()
    for i in List:
        if i in s:
            return i
        else:
            s.add(i)
    return -1


def problem8(n: int) -> dict:
    """a function that gives square and cube of numbers 0 to n
    doctests:
    >>> problem8(3)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27]}
    >>> problem8(5)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27], 4: [16, 64], 5: [25, 125]}
    """

    d = dict()
    for i in range(n + 1):
        l = [i ** 2, i ** 3]
        d[i] = l
    return d


def problem9(no: int, words: list) -> list:
    """Given two lists of equal size, write a function to create tuples of
    each consecutive element having same index.
    doctests:
    >>> problem9([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    >>> problem9([6, 8, 5, 8, 4], ['a', 'b', 'c', 'd', 'e'])
    [(6, 'a'), (8, 'b'), (5, 'c'), (8, 'd'), (4, 'e')]
    """

    result = zip(no, words)
    return list(result)


def problem10(n: int) -> list:
    """a function that uses list comprehension to generate the squares
    of 0 to n.
    doctests:
    >>> problem10(5)
    [0, 1, 4, 9, 16, 25]
    >>> problem10(8)
    [0, 1, 4, 9, 16, 25, 36, 49, 64]
    """
    myList = list()
    for i in range(n + 1):
        myList.append(i ** 2)
    return myList


def problem11(n: int) -> list:
    """a function that uses dictionary comprehension to generate a
    mapping from (0 to n) to their squares.
    doctests:
    >>> problem11(5)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    >>> problem11(3)
    {0: 0, 1: 1, 2: 4, 3: 9}
    """
    d = dict()
    for i in range(n + 1):
        d[i] = i ** 2
    return d


def func(x: str) -> str:
    return x.upper()


def func2(a: int) -> int:
    return a ** 2


def problem12(List: list) -> list:
    """a function makes a class such that the initializer takes an arbitrary list of atomic values as input and saves it
     in an instance variable and has a method called apply which Accepts a function as a parameter, and Applies the
     function to saved list and return the output and if it fails its raises an Exception with a custom error message.
    doctests:
    >>> problem12([1, 3, 5, 8])
    [1, 9, 25, 64]
    >>> problem12(['Aman'])
    Traceback (most recent call last):
    TypeError: Input must be a list of integers
    """
    return p12(List).apply(func2)


def problem13(List: list) -> list:
    """a function takes as input a list of words and upper-cases each
    word.
    doctests:
    >>> problem13(['ab', 'cd', 'ef', 'gh'])
    ['AB', 'CD', 'EF', 'GH']
    >>> problem13(['am', 'an', 'budhrani'])
    ['AM', 'AN', 'BUDRANI']
    """

    return list(map(func, List))


def problem14(List: list) -> int:
    """a function to find the product of all the numbers
    doctests:
    >>> problem14([1, 2, 3, 4, 5, 1, 2])
    240
    >>> problem14([5,4,10,12,8])
    19200
    """

    return functools.reduce(lambda a, b: a * b, List)


class p12:
    myList = list()

    def __init__(self, myList:list):
        self.myList = myList

    def apply(self, funct) -> list:
        try:
            l = list(map(funct, self.myList))
            return l
        except TypeError:
            raise TypeError("Input must be a list of integers")


# input = input("str")
if __name__ == "__main__":
    import doctest

    doctest.testmod()

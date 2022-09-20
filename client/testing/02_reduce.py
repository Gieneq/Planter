import functools
import itertools
from functools import reduce

print(functools.reduce(lambda prev, curr: prev + [sum(prev[-2:])], range(20), [1, 1]))

missing = object()
def myreduce(f, data, start=missing):
    it = iter(data)
    if start is missing:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError('adadasd') from None
    else:
        value = start

    for i in it:
        value = f(value, i)

    return value


# print(myreduce(lambda x,y : x+y, [1,2,3])  )

print(myreduce(lambda prev, curr: prev + [sum(prev[-2:])], range(2-2), [1, 1]))


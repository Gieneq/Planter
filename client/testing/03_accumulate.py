import itertools
import functools

print(functools.reduce(lambda s,c: s+c, range(10), 0))
print(*itertools.accumulate(range(10)))

import math
import itertools

it = itertools.count(0, 2)
print(*(f"{next(it)} : {d}" for d in dir(math) if '' in d), sep='\n')
print(hasattr(itertools, 'count'))
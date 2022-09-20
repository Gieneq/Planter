from factorial import factorial
from itertools import accumulate
import tabulate

lp = list(range(5))
factorial = [factorial(n) for n in lp]
acc = list(accumulate(lp))

labels = ['LP', 'FAC', 'ACC']
data = [*zip(lp, factorial, acc)]
data.append([0,"asdsfdgfhgdfsa", 'asdsfdgfhgdfsa'])

print(data)

print(tabulate.tabulate(data, headers=labels))

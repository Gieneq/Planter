import multiprocessing
import time
import random

print(multiprocessing.cpu_count())

start_time = time.perf_counter()
def dosth(delay=1, i=None):
    print(f'{i}: Start delay {delay} s')
    time.sleep(delay)
    print(f'{i}: End delay {delay} s')

n = 5
procs = []
for i in range(n):
    i = i+1
    p = multiprocessing.Process(target=dosth, kwargs={'delay': i, 'i':i})
    p.start()
    procs.append(p)


for p in procs:
    p.join()

end_time = time.perf_counter()

print(f'Done in {round(1e0*(end_time - start_time), 3)} s')
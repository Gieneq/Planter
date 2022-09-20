import threading
import time


start = time.perf_counter()

t1 = threading.Thread(target= lambda: time.sleep(1))
t1.start()


t1.join()

print('Done')
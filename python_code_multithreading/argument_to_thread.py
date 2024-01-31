from threading import Thread
from time import sleep, perf_counter

def task(id):
    print(f'the process of {id} starts')
    sleep(1)
    print (f'the prcess of {id} finished')

start_time= perf_counter()

threads = []
for n in range(1, 11):
    t= Thread(target=task, args= (n, ))
    threads.append(t)
    t.start()
for i in threads:
    i.join()

end_time= perf_counter()
print (f'it tooks {end_time-start_time:0.2f} second to finish all threads process')
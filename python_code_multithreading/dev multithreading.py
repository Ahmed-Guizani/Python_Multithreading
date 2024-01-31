from threading import Thread
from time import sleep, perf_counter

def task():
    print('message')
    sleep (1)
    print('done')

start_time = perf_counter()
#new thread by instantiating an instance of the Thread

t1=Thread(target=task)
t2=Thread(target=task)

# start the thread by calling the start() method of the Thread instance:
t1.start()
t2.start()

# By calling the join() method, the main thread will wait for the child thread to complete before it is terminated
t1.join()
t2.join()
end_time= perf_counter()

print(f'the process tooks {end_time-start_time:0.2f} second to finish')
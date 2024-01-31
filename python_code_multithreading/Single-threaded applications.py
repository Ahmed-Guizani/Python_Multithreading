from time import sleep, perf_counter
# define a function that takes one second to complete:
def task():
    print('Starting a task...')
    sleep(1)
    print('done')

# get the value of the performance counter by calling the perf_counter() function:
start_time = perf_counter()

task()
task()

end_time = perf_counter()

# output the time that takes to complete running the task() function twice/ for 0.2f to explain that result should ben float x.00
print(f'It took {end_time - start_time: 0.2f} second(s) to complete.')
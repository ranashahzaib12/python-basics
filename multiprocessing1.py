# Processes that run in parallel
#When to use:
#CPU-Bound Tasks... for heavy task managment
#parallwl executiion of multiple cores of the CPU 

import multiprocessing
import time 

 
def squ():
    for i in range(5):
        time.sleep(2)
        print(f'square: {i*i}')

def cube():
    for i in range(5):
        time.sleep(2)
        print(f'Cube: {i*i*i}')


if __name__ == "__main__":
    # Creating two threads 

    p1 = multiprocessing.Process(target=squ)
    p2 = multiprocessing.Process(target=cube)

    t = time.time() 
    p1.start()
    p2.start()

    # Waiting for the processs to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)
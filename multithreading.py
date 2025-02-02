#when to use Multi threading
#** I/O -bound task that spend more time for I/O operations
# ** when we have COncurent Execution: WHen you watn to improve the throughput of the application


import threading
import time

def print_number():
    for i in range(5):
#It's a thread I/O of sleep of 2 seconds  time.sleep(2)
        time.sleep(2) #For each iteration the program will sleep for 2 seconds
        print(f"Number: {i}")

def print_letter():
    for letter in "abcd":
        time.sleep(2)
        print(f"Letter: {letter}")

# If the program sleeps ata ny point which is not a good thing 
# to handle this we use threading of breaking the function if
# programm sleeps at any point
t = time.time()

# Creating two threads 

t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letter)

t1.start()
t2.start()

# Waiting for the threads to complete
t1.join()
t2.join()

# this multi threading reduced/Half the Execution time

# print(print_number())
# print_letter()
finished_time = time.time() - t
print(finished_time)
# Multithreading with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time


def print_number(number):
        time.sleep(2)
        return f"Number: {number}"

numbers =[1,2,3,4,5] #It's speed is fast even with a sleep time of 2 seconds

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number,numbers)


for result in results:
    print(result) 

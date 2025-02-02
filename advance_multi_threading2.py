# Multithreading with processpool xecutor

from concurrent.futures import ProcessPoolExecutor
import time


def square_number(number):
        time.sleep(2)
        return f"square: {number * number}"

numbers =[1,2,3,4,5] #It's speed is fast even with a sleep time of 2 seconds
if __name__ == "__main__":# Entrance point
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number,numbers)


    for result in results:
        print(result) 

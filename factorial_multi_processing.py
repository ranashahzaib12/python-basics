# Factorila calculation 
# fasten the computational worlk to calculate the factorial of the large number
#Just sving the runtime of a code
import multiprocessing , math , sys , time

#Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# Functio to compute factorials of a given number

def computer_factorial(number):
    print(f"computing factorial of {number}")
    result = math.factorial(number)
    return result

if __name__ == "__main__":
    numbers = [5000,6000,7000]

    start_time = time.time()
     
    #Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial,numbers)
    end_time = time.time()


    print(f"Results: {results}")
    print(f"Time taken: {end_time-start_time} seconds")


     
import time



for i in range(1,10):
    number = 10**i
    product, current = 1, 1

    #store starting time
    start_time = time.time()

    # write your while loop here
    while current <= number:
                # multiply the product so far by the current number
        current += 1    # increment current with each iteration until it reaches number
    
    #print(product)
    
    #store ending time
    end_time = time.time()
    print(f'Total runtime of the program {i} with number {number} is {(end_time - start_time):.5f}')
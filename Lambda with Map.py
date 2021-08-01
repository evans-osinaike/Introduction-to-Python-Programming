#map() is a higher-order built-in function 
#that takes a function and iterable as inputs, 
#and returns an iterator that applies the 
#function to each element of the iterable.

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

#def mean(num_list):
#    return sum(num_list) / len(num_list)

lambda_mean = lambda numlist: sum(numlist) / len(numlist)

averages = list(map(lambda_mean, numbers))
print(averages)
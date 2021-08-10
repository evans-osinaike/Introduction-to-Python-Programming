#filter() is a higher-order built-in function 
#that takes a function and iterable as inputs 
#and returns an iterator with the elements from 
#the iterable for which the function returns True.

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

#def is_short(name):
#   return len(name) < 10

is_short = lambda name: len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)
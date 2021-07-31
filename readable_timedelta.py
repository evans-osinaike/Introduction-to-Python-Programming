# write your function here
# function that takes an integer and returns the no of weeks and days in that number
def readable_timedelta(num):
    week = 7
    result = '{} week(s) and {} day(s).'.format((num // week), (num % week))
    return result

# test your function
print(readable_timedelta(10))
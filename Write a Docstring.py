def readable_timedelta(days):
    # insert your docstring here
    ''' Calculate no of weeks and remainder days obtainable from a given value
    
    INPUT:
    days: int. Number of days to calculate for
    
    '''
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
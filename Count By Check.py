start_num = 3#provide some start number
end_num = 3000#provide some end number that you stop when you hit
count_by = 11#provide some number to count by 
break_num = start_num

if start_num > end_num: # write a condition to check that end_num is larger than start_num before looping
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
else:
    while break_num <= end_num: # write a while loop that uses break_num as the ongoing number to 
        break_num += count_by    #   check against end_num
    result = break_num
print(result)
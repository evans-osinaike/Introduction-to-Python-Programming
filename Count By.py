start_num = 3 #provide some start number
end_num = 3000#provide some end number that you stop when you hit
count_by = 14 #provide some number to count by 
break_num = start_num
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
while break_num <= end_num:
    break_num += count_by

print(break_num)
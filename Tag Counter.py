tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    #if "{}{}".format(token[0],token[-1]) == "<>": #Alternate format of the solution
    if f"{token[0]}{token[-1]}" == "<>":
        count += 1
    
print(count)
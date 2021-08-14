def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename, 'r') as f:
        for line in f:
            cast_list.append(line.split(',')[0])

    return cast_list

cast_list = create_cast_list('flying_circus_cast_list.txt')
#print(cast_list)
for actor in cast_list:
    print(actor)
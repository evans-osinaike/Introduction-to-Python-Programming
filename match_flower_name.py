# Write your code here

# HINT: create a dictionary from flowers.txt
flowers = {}
with open('flowers.txt', 'r') as f:
    for line in f:
        single_flower = line.split(': ')
        letter, flower = single_flower[0], single_flower[1]
        flowers[letter] = flower

# HINT: create a function to ask for user's first and last name
def name_to_flower():
    full_name = input('Enter your First [space] Last name only: ')
    #name_letter = full_name.split()[0].split()[0]
    name_flower = flowers[full_name[0].upper()]
    return name_flower

# print the desired output
print('Unique flower name with the first letter: {}'.format(name_to_flower()))

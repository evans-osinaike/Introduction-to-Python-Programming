# TODO: First import the `random` module
import random as r

# We begin with an empty `word_list`
word_file = "word_list.txt"
word_list = []

# We fill up the word_list from the `word_list.txt` file
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# TODO: Add your function generate_password below
# It should return a string consisting of three random words 
# concatenated together without spaces

def generate_password(word_list):
    count = 0 #Iteration counter
    password = ''
    while count < 3:
        #pick random index on the list
        i = r.randrange(0,len(word_list))
        # update the current password phrase
        password += word_list[i]
        count += 1
    return password

# Now we test the function
print(generate_password(word_list))

def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

def generate_password():
    return ''.join(random.sample(word_list,3))
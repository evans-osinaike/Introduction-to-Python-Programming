from os import close


f = open('some_file.txt', 'r')
content = f.read()
f.close()

print(content)

f = open('some_file2.txt', 'w')
f.write("Hello There! \n\nLet\'s keep creating magic together. \n\n Cheers")
f.close()

with open('some_file2.txt', 'r') as f:
    file_data = f.read()

print(file_data)
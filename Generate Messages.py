names =  (input('Input names separated by commas:')).split(sep=',')# get and process input for a list of names
assignments =  (input('Input the number of assignments separated by commas:')).split(sep=',') # get and process input for a list of the number of assignments
grades =  (input('Input the grades separated by commas:')).split(sep=',') # get and process input for a list of grades
zip()
# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "\nHi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

for name, grade, assignment in zip(names, grades, assignments):
    print(message.format(name.title(), assignment, grade, int(grade) + (2*int(assignment))))
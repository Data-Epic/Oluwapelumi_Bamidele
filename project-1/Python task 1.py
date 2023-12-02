''' this program print 'hello world' to the console.
Stores a user name, age, and a boolean value indicating a student or not using
the detail provided by the user. print the values and make creative usage of the
details provided'''

print('hello world')
#functionality added asking the user for details instead of manual input
#variable declared
name = input('enter your name: ')
age = input('enter your age: ')
is_student = input('are you a student(yes/no): ')
if is_student == 'yes':
    is_student = True
else:
    is_student = False
    
#values of the variables printed
print('name: ',name)
print('age: ',age)
print('student identity: ',is_student)

#output creativity: display the user name, age, confirming the student identity
print(name.title(), 'is',age,'years old and the student identity is',is_student,'.')


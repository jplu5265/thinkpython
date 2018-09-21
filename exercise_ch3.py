#Exercises in Chapter 3
#Exercise 3.3

def right_justify(mystring):
    newstring = (70 - len(mystring)) * '*' + mystring
    print(newstring)

# right_justify('My name is Jason Lu')
# right_justify('Jason Lu')

#Exercise 3.4

def print_spam(mystring):
    print(mystring)

def print_twice(arg):
    print(arg)
    print(arg)

def do_twice(f, arg):
    f(arg)
    f(arg)

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

#print_spam('Python')
do_twice(print_twice, 'two_spam')
do_four(print_twice, 'four_spam')

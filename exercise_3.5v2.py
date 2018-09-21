#Exercise 3.5 Drawing Patterns

def print_symbol(sym, val, terminator):
    print(sym * val + terminator,)

def print_break(val):
    #print('val = %s' %val) 
    while val > 0:
        print_symbol('+----', 2, '+')
        val -= 1
        #print('val = %s' %val)

def print_middle(num):
    while num > 0:
        print_symbol(' |      ', 2, '|')
        num -= 1

def do_twice(f, arg1, arg2, arg3):
    f(arg1, arg2, arg3)
    f(arg1, arg2, arg3)

def do_four(g, par1, par2, par3):
    do_twice(g, par1, par2, par3)
    do_twice(g, par1, par2, par3)

print_break(1)
print_middle(4)
print_break(1)
print_middle(4)
print_break(1)

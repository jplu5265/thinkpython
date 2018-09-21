#Exercise 3.5 Drawing Patterns

def print_symbol(sym, val, terminator):
    print(sym * val + terminator,)

def print_break(val):
    while val > 0:
        print_symbol('+----', 2, '+')
        val =- 1

def print_middle(num):
    while num > 0:
        print_symbol(' |      ', 2, '|')
        num =- 1

#do_twice and do_four paramater lists must be distinct, error otherwise

def do_twice(f, arg1, arg2, arg3):
    f(arg1, arg2, arg3)
    f(arg1, arg2, arg3)

def do_four(g, par1, par2, par3):
    do_twice(g, par1, par2, par3)
    do_twice(g, par1, par2, par3)

print_break(2)
print_middle(4)
'''
def do_one_four(h, val1, val2, val3):
    print_symbol(sym, val, terminator)
    do_four(g, par1, par2, par3)

do_one_four(print_symbol, 

print_symbol('+----', 2, '+')
do_four(print_symbol, ' |      ', 2, '|')
print_symbol('+----', 2, '+')
do_four(print_symbol, ' |      ', 2, '|')
print_symbol('+----', 2, '+')
'''

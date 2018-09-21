#Exercise 3.5 Drawing Patterns

def print_symbol(sym, val, terminator):
    print(sym * val + terminator,)

#do_twice and do_four paramater lists must be distinct, error otherwise

def do_twice(f, arg1, arg2, arg3):
    f(arg1, arg2, arg3)
    f(arg1, arg2, arg3)

def do_four(g, par1, par2, par3):
    do_twice(g, par1, par2, par3)
    do_twice(g, par1, par2, par3)

print_symbol('+----', 2, '+')
do_four(print_symbol, ' |      ', 2, '|')
print_symbol('+----', 2, '+')
do_four(print_symbol, ' |      ', 2, '|')
print_symbol('+----', 2, '+')

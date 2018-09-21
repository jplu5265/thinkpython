#Exercise 3.5 Drawing Patterns

def print_symbol(sym, val, terminator):
    print(sym * val + terminator,)

def print_break():
    print_symbol('+----', 2, '+')

def print_middle():
    print_symbol(' |      ', 2, '|')

def do_twice(f):
    f()
    f()

def repeat(f, arg):
    interchange(arg)
    interchange(arg)

def do_four(g):
    do_twice(g)
    do_twice(g)

def interchange(h):
    print_break()
    do_four(h)

repeat(interchange, print_middle)
print_break()

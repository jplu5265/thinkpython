import math

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_twice(print_me):
    print (print_me)
    print (print_me)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

#repeat_lyrics()
#print_twice('Spam ' * 4)
#print_twice(math.pi)
cat_twice('Spam' *4, 'The String')

print("helloooooo")
message = "heyo"
print (message)

name = "colton williams"
print (name) ## this will print as seen
print (name.title())
 ## this will see both words as titles so will capitalise them
print (name.upper()) ## will print in all upper case
name2 = "COlton WilliAms"
print (name.lower()) ## will print in all lower case -  better for info storage

# in multiple parts 
first_name = "Colton"
last_name = "Williams"
full_name = f"{first_name} {last_name}"
# f = format, python replaces values in brackets with variables within 
print (first_name)
print (full_name)
test_name = f"{first_name} {63} {last_name}"
# 63 is another variable so even though it is not an object it can be added 
print (test_name)

longer_message = f"{message} {", from"} {full_name}"
print (longer_message)

# whitespace or a "tab" - to add an extra space to work 
print (first_name, "\t", last_name)
# to remove this 
space = 'words  '
print (space) # has spaces at end 
print (space.rstrip()) #  doesn't 
 
# print a list 
print ("Food:\n\tCarrots\n\tHerbs\n\tMeat") # need \t to split words from eachother
# need \n for newline

## to remove whitespace at the end of a line, add ".rstrip()" to the end of the variable 
# the variable must be adjusted to keep this change:
#eg
message = message.rstrip()
## to remove it from the front of the line use ".lstrip"
# to remove all white space use ".strip"
spaces = ' too many spaces '
print (spaces.strip)

## DO NOT USE APOSTROPHES TO MAKE A VARIABLE IF THE STRING HAS APOSTROPHES

## maths:
# + = plus
# * = times
# - = minus 
# / = divide ----- always gives a float
# ** = powers 
# % = modulo -- gives the remainder of the division
# can use BIDMAS

# if it has a decmimal point = a float - sometimes will be an obscene amount of 0's 
# if one float is involved, the answer will always be a float 
# python will not include underscores if written in a number eg:
number = 4_000 # 4,000  
print(number)

# can assign multiple things at once. eg:
a, b, c = 6, 9, 4 
print (b)

# constants are numbers that never change -- nothing in python to keep
# this so use ALL CAPS to symbolise a number should be a constant eg:
CONSTANT = 678
print (CONSTANT)

import this 


#### lists --- in [] is an example of slicing
# list is a string of outputs where you can isolate one of the variables 
animals = ['cats', 'dogs', 'bats', 'frogs']
print (animals)
# to isolate 
print (animals[3]) # the first variable is counted as '0'
print (animals[0])
# by using negatives, it starts from the end of the list 
print (animals[-1])
### can add this to another variable eg:
me = f"I love to pet {animals[2]}"
print (me)

## adding to a list: use .insert(number, 'variable')
animals.insert(2,'dinosaurs')
print(animals)

## or use append to add directly to the end 
animals.append('koala')
print(animals)

## removing use del at the start followed by list[number]
del animals[2]
print(animals)

## using the pop() method, you can remove a variable while using their value 
drinks = ['coke', 'sprite', 'pepsi', 'fanta']
print(drinks)

popped_drinks = drinks.pop()
print(drinks)
print(popped_drinks)
## fanta is outside, so it is still there but not part of the list
# this can be used by itself then
last_drink = drinks.pop()
print(f"I like {last_drink}")
print(f"I like {popped_drinks}")

## can add a number to pop(_) to remove a specific one 
print(animals)
popped_animals = animals.pop(1)
print(popped_animals)
print(animals)
#### EACH IETM POPPED IS REMOVED FROM THE LIST PERMANENTLY UNLESS READDED
# use pop() if you still want to be able to use the value, del if not

## can remove things that fit certain requirements with .remove - but 
#only one thing at a time by making it it's own variable
things = ['car', 'house', 'bike', 'dog', 'flowers']
too_spenny = 'house'
things.remove(too_spenny)
print(things)

# can sort a list 
things.sort()
print(things) ## auto arranges it alphabetically --- this cannot be undone 
# can be reversed
things.sort(reverse=True)
print(things)

## if wanting to sort a list then the sorted() function can be used instead of sort()
things_2 = ['car', 'house', 'bike', 'dog', 'flowers']
print("This is the OG list:")
print(things_2)

print("This is the sorted list:")
print(sorted(things_2))

print("Returning to OG list:")
print(things_2) ## so this list still exists but an alphabetical list can be provided 
# the (reverse = True) can also be applied here 

# to make a list that's the same as the OG but in reverse:
things_2.reverse()
print(things_2)
#can be undone by doing .reverse() again 

### finding the length of a list 
print(len(things))
# this can be used to find ranges and means for integer lists 
#!/usr/bin/python


#python guide

# good online resources for learning Python:
#       http://docs.python.org/2/tutorial/index.html
#       http://www.tutorialspoint.com/python/index.htm


# on the command line, from any place on the system, can use the command
# python -m pydoc XXX	<-- the XXX meaning what you want to know about.
# This will show exactly what the help menu would show when you are actually
# in the python intepreter using: help(XXX)
# I think the methods listed in the help menu with two underscores in front "__"
# are old and don't work anymore maybe.

# to use the python help menu (help(BLAH)) from the command line:
#   in windows:     python -m pydoc BLAH
#   in linux:       pydoc BLAH

# python -h   <-- shows you command line arguments for python

# from sys import exit      -- this allows you to use the exit(0) function, the
# zero means to abort without error (by convention), any non-zero number can stand
# for a specific user defined error and abort

# IMPORTS
# from sys import exit/argv
# from os.path import exists
# import math
# from random import randint
# import time
# import os				<-- lets your perform file-processing operations(see: Files section)


# VARIABLES #
# 5 STANDARD VARIABLE TYPES IN PYTHON ARE:
#       numbers(int, long, float, complex #'s), strings, list, tuple, dictionary

# VARIABLE SCOPE
# two scopes of variables in python:  global and local
# variables defined inside a function have local scope, otherwise they are global.
# In python you can use any global variables inside a function. But you can't change 
# their value, if you do try to modify the variable Python will create a new local variable
# with that same name. You can access the global variable (print it or use it in calculations)
# as long as you haven't already created a new local variable with the same name 
# previously in the function. 
# In short, you can access global variables from inside a function, but trying to modify
# one will create a new local variable with that name, at which point the global variable
# can't be accessed afterword in the function because the function identifies the local
# variable with that name. So you can access a global variable in a function as long as you
# don't try to modify it.

# DELETE VARIABLES
# use the "del" keyword to delete the reference to a variable:
# del var1, var2

# NUMBERS
# numbers in python are immutable data types, which means that 
# changing the value of a number data type results in a newly
# allocated object.
# numbers data types are: int, long, float, complex
# complex numbers are of the form: a + bj, where j is the imaginary
# number (it is the square root of -1, so same as "i" in math usage.
# i.e.  2j    2.34j   5e+23j
# long numbers are integers of unlimited size, written as an integer
# with an upper case or lowercase "L" after it. i.e. 202020L
# floats may be written in scientific notation, with e or E indicating
# powers of ten. i.e.   32.3e10     23.4+e8

#variables: no type declarations cuz its a scripting language
num1 = 23
myAge = 30

# STRINGS
# subsets of strings can be taken using the slice operator [] and [:]
# indices start at 0 at the beginning and -1 at the end.
# Can do 'print str * 2' to print it twice. print str[2:] prints from 2 to end.

# MULTIPLE ASSIGNMENTS
# python allows for assigning a single or multiple values to multiple variables
# on a single line of code
a1 = b1 = c1 = "twins"
a2, b2, c2 = 23, "triplets", 23.99
# The next line makes a tuple (which don't need parenthesis) of two variables,
# width and height, whose values are initilalized as 640 and 480, respectively.
size = width, height = 640, 480


# OUTPUT
#print function. automatically prints an endline
print '7 years ago i was ', num1, " year old."
# to print without an automatic newline character:
# import sys
# sys.stdout.write("output here")


# docstrings span multiple lines and can be used as either comments or a string.
# When treated as a string it can hold both single quotes and double quotes within it.
""" this is a docstring, it can be used as a
    multi-line comment or can be..."""
print """...printed out to the screen!"""
print '''
When using the 'docstring' to print
	it includes the endlines you put in there
	when you hit "enter" and any tabs that start
	the line.\n'''


""" to insert a variable into a printed string without having to use multiple,
    arguments to the print statement you do the below:"""
print "Hey %s there." % "you"   # inserts "you" into the printed string where %s is
print "michael jordan's number was %s" % num1
print 'AliciaMarie is %s and I am %s' % (num1+1, myAge)


#put this statement below if using non-ASCII characters and get an encoding error
# -- coding: utf-8 --

# %r means to print something with single quotes around it I think
# use %r for debugging b/c it displays the raw data, the others are used for users
# the r stands for representation. only use for debugging, never have in finished
# version.
print 'yo %r man' % 'todd'  # prints: yo 'todd' man

# MULTI-LINE STATEMENTS using the continuation character "\"
aVar = 3 + \
       3 + 5 + \
       10
print 'aVar =', aVar   # prints out 21 because aVar is on all 3 lines

#MULTIPLE STATEMENTS ON A SINGLE LINE use semi-colon
jo = 5; mo = -12; print 'jo + mo is',jo+mo


# RAW STRING
# an r or R immediately preceding a string makes it a raw string, which
# suppresses the meaning of escape characters, so it prints out exactly
# what is literally in the string
# r"yo\tmomma\n" would print out:  yo\tmomma\n


# %r, %s, and %d are formatters
print 'yo %d man' % 55  # %d is to embed integers
sumtin = "hey man %r"
holy = 'holy cow'
print sumtin % holy

# more formatting
formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)		# prints: 1 2 3 4
print formatter % ("one", "two", "three", "four")	# prints: 'one' 'two' 'three' 'four'
print formatter % (True, False, False, True)	# prints: True False True False
print formatter % (formatter, formatter, formatter, formatter)	# prints: '%r %r %r %r' 'same thing 3 more times'
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)	# Third string will appear in double quotes because a single quote is used
	# in the string, so python automatically does the most efficient thing
# more formatting
# %s        string
# %d        signed integer
# %u        unsigned integer
# %c        character
# %e/%E     exponential notation
# %f        floating point real number
# %g/%G	    the shorter of %f and %e
# %%        prints a single literal %
# see more formatting at tutorialspoint.com in the Strings section

# UNICODE STRINGS
# put a u directly in front of the string:    u'Hello Python'

# can concatentate strings while printing
str1 = 'yo man whats up?'
str2 = ' howzer'
print str1 + str2


# can multiply a string while printing to display the string that many times
print '.' * 10


# can use two print statements with a comma ending one of them to print things
# on the same line (the comma just makes a space instead of an endline)
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print end1 + end2 + end3 + end4 + end5 + end6,  # prints: Cheese Burger
print end7 + end8 + end9 + end10 + end11 + end12




# Aliasing
# When you assign an object to another object it doesn't just copy the contents of the object to
# the new object, what it does is create a new reference to the original object. This is aliasing.
# It means that multiple names will point to the exact same object. This is why if you assign a list
# to another list, if you change one of them then both of them get that change, because both aliases
# point to the same object. This is the same for any custom objects.






# GETTING INPUT - use the raw_input() function
print 'how old are you?',  # this last comma makes input appear on same line as output
myAge = raw_input()  # automatically takes all input as a string
print myAge # here adding to myAge would cause an error b/c myAge is a string
# can prompt the user with a string argument to the raw_input() function:
myAge = raw_input("What is your age? ")

# The input() function will try to convert things you enter as if they were Python code,
# but it has security problems so you should avoid it. It assumes the input is a valid
# Python expression and returns the evaluated result to you.
aStr = input('Enter your input: ')
print "Received input is: ", aStr		# typing in [x*5 for x in range(2,10,2)]
#												prints out [10, 20, 30, 40]
# TYPECASTING
# int() or int(x[, BASE]), long() or long(x[, BASE]), float(), complex(real[, imag]),
# str(), repr(), eval(str), tuple(), list(), set(), dict(), frozenset(), chr(),
# unichr(), ord(), hex(), oct() 
print 'now how old are you?',
myAge = int(raw_input())
print myAge + 32	# here myAge is an integer



# MATH STUFF
# ** does exponent, // does floor division
# can do all operators with an equal sign like '//='



# BITWISE OPERATORS
# &   -- binary AND
# |   -- binary OR
# ^   -- binary XOR
# ~   -- binary NOT
# <<  -- binary LEFT SHIFT OPERATOR  ex. a << 2
# >>  -- binary RIGHT SHIFT OPERATOR



# LOGICAL OPERATORS
# AND, OR, NOT



# MEMBERSHIP OPERATORS
# in   <-- true if it finds a variable in the specified sequence, false otherwise
# not in   <-- true if it doesn't find a variable in the sequence, false otherwise

# IS operators
# is  <-- returns true if two operands are not just equal but point to the same object.
# is not  <-- returns true if two operands do not point to the same object
3 is 3                # returns True
4 is 3                # returns False
[1,2] is [1,2]        # returns False
x=[1,2]
y=[1,2]
x is y                # returns False
y=x
x is y                # returns True

# Order of Precedence for Operators:
#   **,  ~+-,  */%//,  +-,  >> <<,  &,  ^|,  <= < > >=,  <> == !=,
#   = %= /= //= -= += *= **=,  is  is not,  in  not in,  not or and



# Command Line Arguments
# sending arguments to the python script and importing modules like sys and argv
# hmm, sys is a module so maybe the below line is saying from the sys module just
# import the argv element or whatever. Note Libraries are called Modules in Python.
# if the wrong number of arguments are used on the command line a runtime error occurs.
'''from sys import argv    # this imports the argument variable, which is contained in sys
script, first, second, third = argv # assigns/unpacks arguments to variables in order
print "The script is called:", script
print "your first variable is:", first
print "your second variable is:", second
print "your third variable is:", third'''  # all commented out for the sake of later code.
# NOTE: command line arguments are treated as strings, need to typecast to change. Also
# note that in Python the first argument is always the script name so the arguments to
# add are really one less than what you unpack in the "= argv" line of code.









''' FILES '''
# Using Files:         open file:				FILE_OBJECT = open(FILENAME[, 'access_MODE'][, buffering])
#                             read file:				FILE_OBJECT.read()
#                             write to file:			FILE_OBJECT.write(string)
#                             empty the file:		FILE_OBJECT.truncate()
#                             move to byte in file:	FILE_OBJECT.seek(byte_to_move_to)
#                             close file:				FILE_OBJECT.close()
# Files are used by through the use of a file object, which is created by the open() function.
# Reading is the default way to open a file. Can also specify what you want to do with
# the file by using 'r','w','a' (append) in the open() function. These are the modes. Add
# a 'b' to the mode for binary files, add a '+' to the mode to allow simultaneous reading
# and writing. These are used like 'r+' 'w+' 'a+' 'rb' 'wb' 'ab'
# Once a file is opened you can use some methods on the file object to get information about it:
#     file.closed         <-- returns true if file is closed
#		  file.mode           <-- returns access mode with which file was opened
#		  file.name	      <-- returns name of file
#		  file.softspace    <-- returns false is space explicitly required with print (don't know what this means)

# DESCRIPTION OF SOME MORE METHODS DONE ON FILE OBJECTS:
# CLOSE() Method flushes any unwritten info and closes file object.
# WRITE() Method writes any string to an open file (note: python strings can have binary data in them too).
# Note that the write method does not add a newline character to the end of the string.
# READ() Method reads a string from an open file. If no argument is given to read() then it will keep reading
# to the end of the file. Giving an argument to read() passes the number of bytes to be read from the file.
# TELL() Method (file.tell()) gives you the current position in the file (where the next read will occur) in
# bytes from the beginning of the file.
# SEEK(OFFSET[, FROM]) changes the current file position. The OFFSET argument indicated the number of
# bytes to be moved. The FROM argument specifies the reference point from where the offset will occur.
# So file.seek(100, 0) means to move the current position to 100 bytes from the 0th byte in the file, so move
# to the 100th byte in the file.  file.seek(0,0) would put the current position back at the beginning of the file.

# FILE AND DIRECTORY PROCESSING USING THE OS MODULE
# need to use: import os
# To rename file:				os.rename(current_file_name, new_file_name)
# To delete file:					os.remove(file_name)
# To create dir:					os.mkdir("newdir")
# To change current dir:		os.chdir("newdir")
# To display current dir:		os.getcwd()
# To delete dir:					os.rmdir("dirName")	<-- all files should already be removed from directory.
#																	Also give full path name to directory, else it just
#																	searches in the current directory.
# LINKS TO WEBPAGE WITH LIST OF FILE/DIRECTORY METHODS
''' http://www.tutorialspoint.com/python/os_file_methods.htm
# http://www.tutorialspoint.com/python/file_methods.htm'''

'''
from sys import argv
script, filename = argv
txt = open(filename)
print "Here's your file %r" % filename
print txt.read()
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()
txt.close()
txt_again.close()
'''		# commented out for the sake of later code
# READING INDIVIDUAL LINES FROM A FILE
''' to read individual lines from a file one at a time use the readlines() function in
the form:		FILE_OBJECT.readlines()
And need to put it into a loop to keep reading lines.'''

# USING FILES MORE
'''
from sys import argv
script, filename = argv
print "We're gonna erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file..."
target = open(filename, 'w')		# open the file
print "Truncating the file. Goodbye!"
target.truncate()					# delete the contents of the file, but contents were
									# already deleted by using the 'w' mode in open()
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print "I'm going to write these to the file."
target.write(line1)					# write to the file inefficiently on many lines
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
# another way to do all of the above lines is this:
target.write("%s\n%s\n%s\n" % (line1, line2, line3))
print "And finally, we close it"
target.close()						# close the file
'''		# commented out for the sake of later code

# COPYING ONE FILE TO ANOTHER
'''
from sys import argv
from os.path import exists
script, from_file, to_file = argv
print "\nCopying from %s to %s" % (from_file, to_file)
# we could do these two on one line too:
indata = open(from_file).read()		# file should auto close after this line is complete
print "The input file is %d bytes long" % len(indata)	# use len() to get # of bytes
print "Does the output file exist? %r" % exists(to_file)	# returns boolean
print "Hit RETURN to continue"
raw_input()
out_file = open(to_file, 'w').write(indata)	# file should auto close after this line'''
# out_file.close()  <-- this would create an error because don't need to close due to
#							the way I did the previous line











''' FUNCTIONS '''
# MAKING FUNCTIONS: 	syntax --		def FUNCTION_NAME(ARGUMENTS):
# first statement in a function can be the function doc using a docstring
def exampleFunc(*args):		# *args as a parameter allows a variable number of arguments
    '''The is the documentation for this function'''
    print "arg1: %r, arg2: %r" % (args[0], args[1])
def exFunc(arg1, arg2):
   print "arg1: %r, arg2: %r" % (arg1, arg2)
exampleFunc(23, 35, 99)
exFunc("yes", 23)

# Higher Order Programming / Functions as First Class Objects
#
# Functions in Python are first class objects, which means that functions can be used as data.
# So functions have a data type, can be an element in a list/tuple, can be arguments to other
# functions.
# This can be used to make a function that does something like takes a list and a function as
# arguments and applies the function to each element of the list using a for-in loop. Then using
# this function you can apply any function to each element of any list by just passing in the
# list and the function as arguments.
# Could also make a list of functions, and make a function that loops through that function-list
# argument to apply all those functions to some value (the other argument).
# powerful stuff.
# Using functions as first class objects is called Higher Order Programming. Python provides some
# higher order functions to use, like map.

# The Map Function:
# Syntax: map(function, list)
# Map takes a function that takes one or more arguments and applies that function to each element
# in the list. It can take n-number of lists. For example:
map(min, [1,-20,18,40], [12,99,-5,38])  # finds the minimum value of each comparable index
# so the above line of code would return [1,-20,-5,38]


# a group of individuals statements making a code block is called a suite
# You can redefine functions later on in the executing code simply by writing a function definition
# for that function same name again in the code.
# Functions should go at the top of the source file (except redefinitions of functions) or they should be
# imported from another python file.

# NOTE: All arguments in Python are passed by-reference. But assigning a new value
# to a variable makes a whole new reference so it doesn't affect the variable on the
# outside of the function. Altering the current value though does change the outside
# variable. Need to test exactly how this works.

# Function Arguments
# Required Argumetns (the normal way), arguments must be in order
# Keyword Arguments:
#      funct(age=50, name='todd')   <-- args can be out of order
# Default Arguments:
#      def funct(name, age=30):  <-- default value for arg if none is given in call
#      funct(name='joe')    <-- age defaults to 30 in this case
# Variable-length Arguments
#       syntax:  def funct([formal args,] * var_args_tuple):
#       i.e.  def funct(arg1, *vartuple):       <-- vartuple is a tuple to be used

# Anonymous Functions using the LAMBDA keyword
# called anonymous because they have no function name. Also they are not declared with the
# def keyword. Lambda/Anonymous functions are small one line statements.
# Lambda forms can take any number of arguments, but return just on value as an expression
# Lambda can't be a direct form to print because lambda requires an expression
# Lambda functions have their own local namespace so cannot access variables other than 
# the function arguments and those in the global namespace.
# syntax:      lambdaFuncName = lambda [arg1 [, arg2,...argn]] : expression
sum = lambda numA, numB: numA + numB
print 'labmda function gives:', sum(23,9)


# RETURNING THINGS FROM FUNCTIONS
def doSomtin(yo):
    return yo,'wzer'		# you can return two things from a function by using a comma
print doSomtin("todd")		# prints: ('todd', 'wzer')
ret1, ret2 = doSomtin("whatevs")	# also return multiple things to multiple variables
print "ret1: %s, ret2: %s" % (ret1, ret2)

def doSome(x):
    return x*2
double = doSome(54)
print double










''' MODULES '''
# A Python Module is a library in python. It is simply a file consisting of python code that
# defines functions, classes, and variables. It can also include runnable code.
# There are plenty of Python modules to use by importing them via the  line of code:
'''		syntax:		import MODULENAME [, module2[,... moduleN]]'''
# You can make you own modules as well and import them the same way, but don't
# include the ".py" at the end of the file name in the import statement.
''' Using syntax:   from MODULE import ELEMENT[, element2[,...elementN]]       imports'''
# only specific parts of the module instead of the whole thing. Do this if you are only
# using a couple things from the module to keep your file size down and make the
# program run faster. Can also use:     from MODULE import *     to import everything
# and not have to put the name of the module with a dot operator when using it's
# methods, but use this sparingly. Not sure why it's not a good idea to use it.

# IMPORTING YOUR OWN FILES, MAKING YOUR OWN MODULES
# You write a python script and import it into another python script. Do this by using
# the import keyword with the filename (not including the '.py'). See file tryEx25.py
# which imports ex25.py
# When you run the file that imports another file, the imported file creates a module
# with the same name as the file being imoprted but it ends with a .pyc, the 'c' stands for 'compiled'.
# You can now see the homemade module in the help() menu in python or by using the
# "python -m pydoc WHATEVER" command. It shows all the function names with arguments
# and anything that was commented in docstrings, which are used to describe the functions.

# NAMESPACES
# Variables are names (identifiers) that map to objects. A namespace is a dictionary of
# variable names (keys) and their corresponding objects (values). A Python statement
# can assess variables in a local namespace and in the global namespace. If a local and
# global var have same name the local var shadows the global var. Each function has its
# own namespace. Python assumes any variable assigned a value in a functin is local.
# Can make a global variable in a function using the keyword:   global
# When using the global keyword you cannot set the value of the variable, only declare it.
def funkytown():
    global myGlobalVar
    myGlobalVar = 100
funkytown()
print 'myGlobalVar:', myGlobalVar    # prints out 100, which was set inside the function
# dir(MODULE) function gives a sorted list of all the modules, variables, and functions defined
# in the module.
import math
print 'Math Module:\n', dir(math)
# in the list the __name__ is the module's name, and the __file__ is the fiilename from which
# the module was loaded.

# GLOBALS() AND LOCALS() FUNCTIONS
# globas() and locals() when called from within a function shows what global and local
# variables can be accessed from that function. The return type is dictionary, so the variable
# names can be extracted using the keys function.
def localsFun():
    jony = 'to'
    print 'locals:\n', locals()
    print 'globals:\n', globals()
    print 'globals names:\n', globals().keys()
localsFun()

# RELOAD() FUNCTION
# to re-import a module, after it's already been imported once (not sure why you would need to
# do this) use the reload() function.
#		syntax:		reload(MODULENAME)

# NOTE ON IMPORTING
# if you replace the import line of "import MODULE" with "from MODULE import *" then
# you don't have to include name of the module with dot format "MODULE.FUNCTION()"
# whenever calling a function from it. the * means "all".
# Compare the follow two ways to import the math module and use a function in it.
'''
import math
print math.pow(12,2)

from math import *
print pow(12,2)
'''

# round() function
print round(4.55)   # prints: 5.0
print round(4.49)   # prints: 4.0










''' BRANCHING STATEMENTS '''
if 12 < 50 or 15 > 40:
    print "less than"
elif 1 == 1 and 2 != 3:
    print "equal to"
else:
    print "neither"
x=8
if x in range(1,10):        # 1 <= x < 10, inclusive of min, exclusive of max
    print "x is in there"









''' LISTS (WHAT ARRAYS ARE CALLED IN PYTHON) '''
# Methods of lists: append(), count(), extend(), index(), insert(), pop(), remove(),
# reverse(), sort()
# to copy a list do this:   result = list[:]    <-- to splice the whole list
people = ['todd', 'alicia', 'xun', 'lies', 'molly', 'deep']
mixed = [1, 'stephanie', 2, 'julia', 3, 'ann']		# can have a mixed type list
elements = []			# define an empty list and build later in a loop below
# make a 2D List like:      list = [[2,4,5],[3,1,9]]
# to access a specific element in a list:
gotcha = mixed[3]
print 'this is gotcha', gotcha
print mixed[1:4]        # this accesses the elements at index [1,2,3]
# use del keyword to delete an element whose index you know
listy = ['aunt', 'jemima', 'maple', 'syrup', 'todd', 'dabest']
print 'the list listy is:', listy
del listy[3]                # deletes 'syrup' from list
# use remove() function to delete an element whose index you don't know:
listy.remove('jemima')      # deletes 'jemima' from list
print 'the list listy is:', listy

# Syntax:  "string"[startIndex : endIndexExclusive : iteratorInterval]
print 'toddkrone'[::2]  # prints "tdkoe"
print 'toddkrone'[::-1] # reverses the string: "enorkddot"

# things you can do to a list:
len(listy); len([1,4,123,9])        # get length of a list
[23, 34, 1, 'jfj'] + ['yo', 2]      # concatenate lists (makes new list)
['Hi', 'Python'] * 3                # repeat lists (makes new list)
'dabest' in listy                   # check membership
#for i in listy:                    # and iteration using a for-in loop

# to copy a list:  list1 = list2[:]
# to make a list point to the same exact memory location as another, and therefore the two are
# linked so when one changes the other changes even after the assignment:     list1 = list2

# splicing a list down to one element still returns a list, not the element by itself, just a list
# of one element.

# Using range() just by itself (i.e. range(n)) prints out a list that is a range of n integers
# from 0 to n-1.
# Syntax:       range(n)      or        range(startInt, exclusiveEndInt, iterationStep)
# The default step is 1, can make a range in descending order using a negative step.
print range(5)        # prints: [0,1,2,3,4]
print range(3,6)      # prints: [3,4,5]
print range(2,10,3)   # prints: [2,5,8]
print range(10,5)     # prints: []
print range(10,4,-1)  # prints: [10,9,8,7,6,5]

# Using sum() you can sum all elements of a list if the list consists of only number data types.
# Syntax:     sum(list)

# FUNCTIONS FOR LISTS
# cmp(list1, list2)
# len(list)
# max(list)
# min(list)
# list(seq)     <-- converts a tuple into a list

# METHODS ON LISTS
# list.append(obj)      <-- no return value, just changes the list
# list.count(obj)       <-- returns the number of occurences of the object (the value given)
# list.extend(seq)     <-- appends sequence to list, returns no value, just changes the list
# list.index(obj)      <-- returns lowest index in list in which object appears
# list.insert(index, obj)   <-- no return value, just changes the list
# list.pop(obj=list[-1])    <-- eliminates and returns last element of the index, or specified index 
# list.remove(obj)      <-- removes the object (value) specified
# list.reverse()      <-- reverses the order of the list in place, but doesn't return a value
# list.sort([func])   <-- sorts objects of list, use compare function if given

# Something called a list comprehension, where you can type cast all the elements in a list in one line
# of code like so:
# Syntax:  returnedList = [typecast(i) for i in list]
someList = ["1","10","100","2","5","98"]
someList = [int(i) for i in someList]







''' TUPLES '''
# Tuples are like Lists but are enclosed in parentheses instead of brackers and are
# basically Constant versions of lists, in that they are read-only; they cannot be
# altered after creation. Tuples can be though of as read-only lists.
# This just means you can't change the values that are already in the tuple, but you can still,
# say, set that tuple variable to a slice of the current tuple, add elements to the tuple, etc.
tuple = (43, 35.34, 'yoMove')
# Note that a series of things assigned to a variable is treated as a tuple even without parens:
tup = 243, 22.22, "yowzers"     # this is a tuple too
print tuple
print tuple[1:3]        # prints: (35.34, 'yoMove')
# tuples don't have to be defined with parens:
tup1 = 'jd', 1, 42, 'ij'
tup2 = ()               # empty tuple
tup3 = ('onetup',)      # a single-value tuple still must have a comma
# can make new tuples out of old ones
tup4 = tup1 + tup3
# delete a tuple with del keyword
del tup3
# tuples have the some operations done to them as strings like len(),
# concatenation, repetition (with *), membership checks, iteration, and slicing.
# Functions operating on tuples:
# cmp(tup1, tup2)
# len(tup)
# max(tup)
# min(tup)
# tuple(seq)      <-- converts a list into a tuple

# for a tuple that has a tuple inside it, you can reference the outer tuple element through an index,
# and then reference the inner tuple element with a second index, like a multi-dimensional array.
# You can also use a second index reference to get at particular characters of a string that is
# in a tuple.
tup5 = (1, 'yo', ('a', 'b', 90), True)
print tup5[2][2]                          # will print: 90
print tup5[1][-1]                         # will print: 'o'

# When taking a slice of a tuple, if you just take a single element (a singleton), what is returned
# isn't that element's data type, a tuple of one element (a singleton) is what is returned.
print tup5[0:1]                           # prints: (1,)

# Can walk through a tuple with a for-in loop

# Using the syntax:  value in tuple      you can check for membership in a tuple, returning a boolean.
1 in tup5       # returns True because there is an element 1 in the tuple
'yo' in tup5    # returns True because 'yo' is an element in the tuple
90 in tup5      # returns False because 90 is inside a tuple element within tup5
90 in tup5[2]   # returns True
True in tup5    # returns True

# A Singleton is a tuple that is just one element.
# To make a singleton you just make a tuple with one element and a comma after that element.
# The comma lets Python know that it is a singleton (a tuple) rather than just a single item.
sing1 = (1,)
sing2 = ('tiny',)
print sing1+sing2










''' LOOPS '''
# FOR LOOP
# syntax:   for ITERATING_VAR in SEQUENCE:   STATEMENTS
# can place a for loop and its body all on one line if the boy is
# a single line, same with while-loops:
for word in ['yo','mo','jo']:  print word
for letter in "Kronenberg":
    print "Current Letter:", letter
for name in people:
    print "A friend is %s" % name
for x in mixed:
    print "I got %r" % x	  # need to use %r because the list has integers and strings
for x in range(0,10):			# fills list indices 0 through 9. 10 total elements
    elements.append(x+4)
for x in range(2,10,2):		# (start, finish (excluded), incrementation)
    print x
for i in elements:
    print "Element was: %d" % i
# range syntax:		range(start, stop, step)
# step is optional, a step of 2 would increment by two each time. The range goes from
# start to stop-1

# can use range() to iterate a for loop through a sequence index
for i in range(0,10):		# this is a typical for-loop in other languages: for(i=0;i<10;i++)
    print i						# prints 0 thru 9
# here using range and length of a list to iterate through it starting  at index 2. Without the
# 2 in the range arguments it would just iterate straight thru the whole list
pies = ['apple', 'banana cream', 'cherry', 'upside-down pineapple', 'blueberry']
for index in range(2, len(pies)):
    print 'Pie: ', pies[index]

# can use an ELSE statement with a for-loop and while-loop. The else statement executes
# after the for-loop exhausted iterating the list. So you would do it where if the loop
# goes all the way through you want a specific thing to happen, this would go in the
# else statement, whereas if some desired thing happened in the for-loop you would use
# the break keyword to break out of the loop in which case the else statement wouldn't
# run. In a while-loop the else statement executes when the condition becomes false,
# again, it is used when you have a break to leave the loop if some desired thing
# happens in the loop, the else statement only runs if the desired thing didn't happen.
# An example in pseudo-code:
#		for all items a character has:
#			if item picked up is new then add it to inventory and break out of loop
#		else:
#			execute what happens if item wasn't found

# PUT A FOR-LOOP INSIDE A LIST INITIALIZATION
someList = [x*5 for x in range(2,10,2)]		# creates a list called someList: [10, 20, 30, 40]
print someList

# Can also use loops in the middle of a line of code like:
# someFunc(item, arg) for item in list


# WHILE LOOP
i=0
numbers=[]
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
print "The numbers: "
for num in numbers:
    print num
# break      <-- terminates inner-most loop
# continue   <-- inner-most loop skips rest of body and start next iteration
# pass       <-- place holder to represent block of code that's currently empty.










''' DICTIONARIES (called dict in python, called hashes in other languages)'''
# dictName = {key:value, key:value, etc}
# del dictName[key]  <-- to delete a pair
# Dicts do not have any order; the elements are unordered.
# The keys must be an immutable object, which is any literal like a number,string,tuple (not a list).
# Look at file dictionaryEx.py for an example of using a dictionary
# dictName.items() gives a list of key,value pairs
# NOTES ON KEYS: keys must be immutable, so they can be strings, numbers,
# or tuples.
# NOTES ON VALUES: values can be anything, including user-defined objects.
print "\n\nDICTIONARIES"
stuff = {'name':'Todd', 'age':30, 'weight':160, 1:'one'}
print stuff
print stuff['name']   # prints:  'Todd'
print stuff[1]        # prints:  1
del stuff['weight']
print stuff
print ''
dict1 = {}      # empty dictionary
# updating/adding to a dictionary
dict1['3k time'] = '9:04'       # adding an entry
dict1['3k time'] = '8:45'
# Removing stuff from dictionaries
del stuff['age']        # remove entry with key 'age'
stuff.clear()           # empty the whole dictionary
del stuff               # delete the entire dictionary
# Can iterate over dictionaries
# for e in dictionary:

# Functions for dicts:
# cmp(dict1, dict2)     len(dict)       str(dict)

# Methods used on dicts:
# dict.clear()
# dict.copy()
# dict.fromkeys()   <-- creates new dict with keys from seq, values set to value
# dict.get(key, default=None)   <-- for the key, returns value or default
#                                   if key not in the dict
# dict.has_key(key)
# dict.items()          <-- gives all item-pairs in a dict
# dict.keys()
# dict.setdefault(key, default=None)    <-- similar to .get, but sets value
#                                       to default if key is not in dict
# dict.update(dict2)        <-- adds dict2's key-values pairs to dict
# dict.values()











''' EXCEPTIONS '''
# Python provides two ways to handle unexpected errors: exception handling and assertions.
# An exception is a Python object that represents an error, the exception must
# be handled immediately or it will cause the program to terminate.
# If you have code that you think might raise an exception, you can use exception
# handling (in the form of a try-except block) to defend against the program terminating.
# There are different kinds of Exceptions to use in Python depending on the type of error. Have to
# manually put in the kind of Exception. Look online to find the different kinds of Exceptions.
# Here are several of the types of Exceptions: IOError, NameError, TypeError, ValueError,
# AttributeError, SyntaxError, KeyError.

# Raise keyword
# Can use a raise clause to raise an excpetion.
# Syntax:     raise Exception("error message")

# A list of Python exceptions to use is here:
'''					http://www.tutorialspoint.com/python/standard_exceptions.htm'''
# Syntax for try-except clause
'''	try:
#			Do some operations here that might cause an error
#		except Exception1Type, e:
#			If there is this Exception, then execute this block
#		except ExceptionType, e:
#			If there is this Exception2 then execute this block
#		else:
#			If there is no exception then execute this block'''
# Note that there is a generic except clause that handles any exception. To do it
# you merely put:          except:				without any sort of type of Exception. This,
# however, isn't considered good programming because it doesn't help the programmer
# identify what the root cause of the problem is.
# You can put multiple types of Exceptions in a single except clause.
''' Syntax:				except (Exception1[, Exception2[,...ExceptionN]]):'''
# The else-block is a good place to put code related to the try-block that doesn't need
# the try-block's protection. Or it could just be where you put a statement to print out
# that the operation was completed successfully.
# Try-except blocks should be used for such things as opening files, writing to files,
# and other stuff like that which might not work.
# The Try-Finally clause is for when you need code that must always execute, whether
# or not the try-block raised an exception or not, and this is what goes in the finally-block.
'''  Syntax for try-finally clause:
#			try:
#				try to do whatever operations here
#				if an exception occurs this block will be skipped
#			finally:
#				This block will always get executed'''
# Exception Argument
# An exception can have an argument that can supply additional information about the exception.
# You capture an exception's argument by supplying a variable in the except clause like this:
'''			except EXCEPTIONTYPE, ARGUMENT:
#				  You can print the value of the Argument here'''
# If you are trapping multiple exceptions in a single exception clause you still just use one variable.
# The variable can receive a single value or multiple values in the form of a tuple. The tuple
# usually contains the error string, error number, and an error location.

# Just using except by itself, with no ExceptionType, means that it'll pick up all exceptions, or
# all other exceptions that occur besides the ExceptionTypes that are specifically called for
# earlier in the try-except block.

# The user can also make their own exceptions. See "Raising an Exception" and "User-Defined
# Exceptions" at the bottom of here:  http://www.tutorialspoint.com/python/python_exceptions.htm

# Assertions
# Can use an assert clause to make sure something is as it is expected to be, otherwise it raises
# an AssertionError. You can't control the error response, it will just raise the AssertionError.
# Using assertions is good defensive programming.
# When an AssertionError is raised, the assertion error message, which comes after the comma in the
# assert clause, will print out and execution will halt.
# Syntax:
#             assert statementToAssert, errorToPrintOtherwise
# i.e.
#             assert x != 0, 'x was zero'
#
# Assertion is a great way to make sure some value is valid before attempting to do anything with it.
# Assert clauses can be used as a more concise way of catching errors than try-except blocks in some
# cases.
# You should rely on raising excpetions for bad user inputs, but use assertions for stuff like:
#       - checking types of arguments or values
#       - checking that invariants on data structures are met
#       - checking contraints on return values
#       - checking for violations of contraints on procedure (i.e. no duplicats in a list)
#
# Assertions can be read about here:  http://www.tutorialspoint.com/python/assertions_in_python.htm










''' CLASSES '''
# class definition header  -->       class myClass(arguments):
''' Note: I think the argument in the class header is only actually needed for inheritance,
    and you don't need to put (object) when there is no inheritance. '''
# When the class isn't a child of another class (no inheritance) then the argument
# used is the word: object. So an un-inheriting class inherits the 'object' class to
# set itself up as an object. Otherwise you tell the class what classes it inherits.
''' instantiate a class (make an object)     -->      myObj = myClass(argsForConstructor) '''
''' constructor:    -->     def __init__(self): '''
#       the constructor makes a self variable which is that empty object inside
#       the class definition. assign variables with self.var = 'blahblah'
# A class variable can be set declared by just initializing a variable name in the class, outside
# of any method or constructor.
''' Syntax for Class creation:
class Person:
    'In here you put a string on the first line of the class to serve as the class doc'
    CLASS VARIABLES  <-- shared by all objects of the class, public (ex. personCount)
    def __init__(self, name, height):
        self.name = name
        self.shape = height
        Person.CLASSVARIABLES = blahblah

    def displayCount(self):
        print "Total people %d" % Person.personCount

    def displayPerson(self):
        print "Name:", self.name, ",   Height:", self.height
'''
# Access the object's variables and methods using the dot operator.
# Add, remove, or modify attributes of classes and objects at any time.
''' PersonObject.age = 39      <-- 'age' was added as an attribute
    PersonObject.age = 20      <-- 'age' attribute was modified
    del  PersonObject.age      <-- 'age' attribute was deleted
'''
# Some functions to be used on objects (not methods of the object):
''' getattr(obj, attrName)    <-- returns value of attribute
    hasattr(obj, attrName)    <-- returns true if attribute exists
    setattr(obj, attrName, value)    <-- set value of attribute
    delattr(obj, attrName)    <-- delete attribute
'''
# Built-in Class Attributes
# these variables are class attributes that can be accessed by:  ClassName.attrName
# __dict__    <-- Dictionary containing the class' namespace
# __doc__     <-- Class Documentation string or None if undefined
# __name__    <-- Class name
# __module__  <-- Module name in which the class is defined (__main__ in interactive mode)
# __bases__   <-- a possibly empty tuple containing the base classes

# Garbage Collection
# Python automatically deletes objects when their reference count reaches zero.
# The destructor, __del__() is invoked when the instance is about to be destroyed. You
# can write your own body for the destructor to have it, other than destroying, say, print
# out the class name of the object being destroyed.



# INHERITANCE
# if you put the keyword 'pass' alone as the code block in a class you are telling
# python that you want to leave that class blank (probably cuz it inherits everything
# from its parent).
# to override a parent function in the child you just make the same function name in
# the child with different functionality.
# To have an overridden child function also call the original parent function you
# put this line in it:              super(childClassName, self).functionName()
# Need to call the constructor on the parent class inside the derived class constructor like so:
#       def __init__(self, othervars):
#           ParentClassName.__init__(self, othervars)
# To use any parent method, as opposed to the instance method of the derived class, you just need
# to use the parent class name as shown for the constructor above when calling it.

# MULTIPLE INHERITANCE: a class that inherits from on or more classes, like:
# class myClass(Parent, anotherParent):     block of code below blahblah

# COMPOSITION
# instead of using inheritance you can use composition by making not a parent class
# but merely another class that the no-longer-a-child class uses. So the non-child
# class is composed of this other class. Can create an instance of that other class
# in the non-child class by defining an object in its constructor like:
'''   def __init__(self):
#       self.other = Other()
#       then use the self.other variable.'''
# Use the issubclass(sub, sup) boolean function to check if "sub" is a subclass of "sup"
# Use the isinstance(obj, Class) boolean function to check if "obj" is an instance of "Class"
# or is an instance of a subclass of "Class"
# Override parent class methods simply by making the exact same method in the child class,
# with different functionality.
# __init__(self)  <-- Constructor, call with:     obj = className(args)
# __del__(self)  <-- deletes an object, call with:     del obj
# __repr__(self)  <-- evaluate-able string representation, call with:    repr(obj)
# __rstr__(self)  <-- printable string representation, call with:     str(obj)
# __cmp__(self,x)  <-- object comparison, call with:     cmp(obj,x)

# Overloading Operators:
# Overload an operator some you can do calculations between objects in whatever way you want
# just using the normal operators. For instance, overloading the __add__ function puts that
# functionality in the '+' operator.
# __lt__    -   less than (specify this to use sort() method on a list with your own custom objects)

# Data Hiding:
# You can hide an object's attributes(variables) so they are not visible outside
# the class definition by putting a double underscore before the attribute name.
''' Syntax for a hidden class attribute:        __attrName = blahblah '''
# You can print the hidden variable through a class/object method, but you can't access it
# in the normal way, public way (which will cause an error. But you still can by instead
# putting the Class name with one underscore before the attribute name:
''' Syntax:        obj._className__hiddenVar '''


# Generators:
# Any method that has a yield statement in it is a generator. Can have multiple yield statements in
# a generator.
# Syntax:       def genName():
#                  # code...
#                  yield returnValue
#                  # code...
#                  yield returnValue
#                  # etc.
# To make an instance of a generator:                           foo = genName()
# Calling next:                                                 foo.next()
# Yield returns the value specified after the yield keyword.
# A Generator is a class, so every instance of a generator has a next() method. This method is
# used to start/resume execution of the method from the line immediately after where the yield
# statement that stopped it is in the method (or from the start of the generator if it hasn't
# been run yet.
# So when a generator's next() method is called the first time it starts executing code from the
# beginning until it reaches a yield statement, the yield suspends execution and returns a value.
# Calling the next() method on the generator again will resume execution from where it left off,
# which will continue until it hits the next yield statement. Each call to the next() method will
# do this until it reaches the end of the generator, at which point returning from the generator
# raises a StopIteration exception.
# Can use a loop inside generator, and put a next() call to the generator inside a loop, and it
# will keep executing and calling yield until it gets to the end of the generator, at which point
# it raises the exception. This allows you to return a value at any point in the method (the
# generator) that you want, but keep the method going so it can finish the task. A normal method
# can't do this because one it is returned the method must start over on the next call.
#
# For example, could have a generator that computes fibonacci numbers, which has a loop in it and
# a yield statement in the loop, with the loop just set to True to keep going, to print out each
# fibonacci number. While the loop that contains the generator.next() statement will keep calling
# the generator so you can keep getting fibonacci numbers, and that outside loop can control how
# many times to call the generator.next() so it controls how many fibonacci numbers are calculated.
#
# Generators separate the concept of computing a long sequence of objects, from the actual process
# of computing them explicitly. Allow you to generate each new object as needed as part of another
# computation, rather than computing a very long sequence only to throw most of it away while you
# do something on an element, then repeat the process. So if you want to work with each individual
# item that is computed in a long list, you can do that by returning it with yield, doing some
# computations, and then getting the next item with another call to the generator.next() that will
# return the next item with yield.








''' REGULAR EXPRESSIONS '''
# the "re" module provides full support for Perl-like regexs in Python. So do:    import re
# The "re" module raises the exception re.error if an error occurs while using a regex.
# When dealing with regexs we use Raw Strings in the form:      r'expression'

# re.match() function:
# The match() function from the 're' module is used to match a regex pattern to a string
# ONLY at the beginning of that string.
'''   Syntax:			re.match(pattern, string, flags=0)'''
# The Pattern argument is the regex to be matched
# The String argument is the string to be searched for the pattern at the beginning of it.
# The flags arguments are optional, can specify different flags with bitwise OR "|". These
# are modifiers listed below:
# re.I				<-- case-insensitive matching
# re.L				<-- interprets words according to current locale. (look up for more details)
# re.M			  <-- makes $ and ^ match the end and beginning of the line, not just of the string
# re.S				<-- makes a period (dot) match any character including a newline
# re.U				<-- interprets letters according to Unicode character set
# re.X				<-- ignores whitespace and treats unescaped # as a comment marker (look up details)

# Match Object Methods
# The re.match() and re.search() functions returns a match object on success, and None on failure.
# Like:
''' Syntax:         matchObject = re.match(pattern, string, flags=0)'''
# Use MatchObject.group() to get entire match
# Use MatchObject.group(num) to get a specific subgroup of the match
# Use MatchObject.groups() to get all matching subgroups in a tuple, which is empty if no match.
# Can use a matchObject in an if statement as a boolean like so:     'if matchObject:'

# re.search() function:
# The search() function searches for the first occurrence of the regex pattern anywhere in a string.
''' Syntax:      re.search(pattern, string, flags=0)'''

# re.sub() function:        Search and Replace
''' Syntax:         re.sub(pattern, replace, string, max=0)'''
# The sub() method replaces all occurrences of the regex pattern in the string with the replace
# argument, substituting all occurrences unless max provided. The method returns the modified string.
# See this webpage for all the Python regex characters to be used in the patterns:
''' http://www.tutorialspoint.com/python/python_reg_expressions.htm '''



## SEE EXERCISE 37 FOR A LOT OF KEYWORDS AND OTHER STUFF TO LOOK UP




# TIME MODULE  -- import time  (import calendar to use calendar)
import time
tick = time.time()      # number of ticks (sec) since 12am, 1/1 1970 (a float)
# dates before 1970 and after sometime in 2038 don't work with these ticks.
# Many of python's time functions handle time as a tuple of 9 numbers:
# 4-digit year, month, day, hour, minute, second, day of week, day of year,
# daylight savings
# the above tuple is equivalent to struct_time:
# tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst
timeNow = time.localtime(time.time())     # gives the fulle tuple local time
print timeNow
timeNow = time.asctime(time.localtime(time.time()))
print timeNow       # displays:  Mon Sep 23 22:21:52 2013
# to display a calendar (need to import calendar):
import calendar
cal = calendar.month(2013, 9)
print cal
# There's a bunch of "time." methods in the time module, look at tutorialspoint.com
# one to sleep is:   time.sleep(secs)
time.sleep(2)
# There's also a bunch of "calendar." methods in the calendar module.



while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,

# SOME USEFUL FUNCTIONS
"""
sorted(iterable_list/string)	: returns a new sorted list
string.split('delimiter')		: returns a list split up by the given delimiter
string.pop(0)					: pops the FIRST word off the string and returns it
string.pop(-1)    or pop()		: pops the LAST word off the string and returns it
print ' '.join(list)            : joins a list into a string with spaces between items
print '#'.join(list[2:4])       : joins a list into a string with hashes between items
"""
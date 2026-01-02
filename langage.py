# *****************************************************************************
# LIBRARIES & IMPORTS
# *****************************************************************************
# In C: #include <stdio.h>
# In Python: we use 'import'
from sys import read, exit
# or
from sys import *
# Include all function in 'sys'
# or
import sys
# But fi use read for example, you must use same this "sys.read()"
# ______________________________________________________________


# *****************************************************************************
# VARIABLES & DATA TYPES
# *****************************************************************************

# Python is Dynamically Typed (No need to declare 'int' or 'char')
integer_val = 10
string_val = "Python handles types automatically based on the value"
# ______________________________________________________________

# Multi-line strings (Similar to long comments or blocks of text)
description = """
In Python, variables are labels to objects in memory,
unlike C where variables are fixed memory locations.
"""
# ______________________________________________________________


# *****************************************************************************
# PRINT FUNCTION (The 'printf' of Python)
# *****************************************************************************

# 1. Simple Print
print("This is how we print a string")
# ______________________________________________________________

# 2. Concatenation (Using + only works with strings)
print("Part A " + "and " + "Part B")
# ______________________________________________________________

# 3. F-Strings (Modern & Fast - similar to printf with %d, %s)
print(f"Displaying variables: {integer_val} and {string_val}")
# ______________________________________________________________

# 4. Comma Separation (Automatically adds a space)
print("Automated space:", integer_val, string_val)
# ______________________________________________________________

"""
	# Note:
		+ print function add new line automatic.
        + How can remove this feature?
			~ print("print without new line", end="").
        + end="":
			~ can be chenge "" to any thing same this:
				- print("can be print and end with any thing same this", end="end of line\n").
"""
# ______________________________________________________________


# *****************************************************************************
# CONDITIONAL STATEMENTS (IF/ELIF/ELSE)
# *****************************************************************************

# Python uses indentation (spaces) instead of curly braces {}
x = 10
y = 20

if x < y:
    print(f"{x} is less than {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is greater than {y}")
# ______________________________________________________________


# *****************************************************************************
# OPERATORS REFERENCE
# *****************************************************************************

#COMPARISON OPERATORS:
#	==	:	Equal to
#	!=	:	Not equal
#	<	:	Less than
#	>	:	Greater than
#	<=	:	Less or equal
#	>=	:	Greater or equal
# ______________________________________________________________

#LOGICAL OPERATORS: (Written as words, unlike C's &&, ||, !)
#	and	:	Logical AND
#	or	:	Logical OR
#	not	:	Logical NOT
# ______________________________________________________________

#ARITHMETIC OPERATORS:
#	+	:	Addition
#	-	:	Subtraction
#	*	:	Multiplication
#	/	:	Division (Always returns a float, e.g., 5/2 = 2.5)
#	//	:	Floor Division (Returns integer, e.g., 5//2 = 2)
#	%	:	Modulus (Remainder)
#	**	:	Exponentiation (Power)
# ______________________________________________________________

#ASSIGNMENT OPERATORS:
#	+=, -=, *=, /=, //=, %=, **=
# ______________________________________________________________

#INCREMENT/DECREMENT:
#	Python DOES NOT have ++ or --. 
#	Always use: x += 1
# ______________________________________________________________


# *****************************************************************************
# LOOP
# *****************************************************************************

# 1.WHILE LOOP: Standard conditional loop
counter = 0
# In C: while (counter < 5) { ... }
while counter < 5:
    print(f"Counter is: {counter}")
    counter += 1  # Remember: No counter++ in Python

# ---------------------------

# Loop in list or string
# In C: while (str[i] or i < sizeof(arry)) { ... }
counter = 0
string = "//."
list = [30, 12, 2006]
while counter < 3:
    print(f"{list[counter]}{string[counter]}", end="")
    counter += 1  # Remember: No counter++ in Python
# Output: 30/12/2006.
# ______________________________________________________________

# 2.FOR LOOP: Using range() to mimic C-style loops
# Loop from 0 to 4 (Stop is exclusive)
# In C: for (int i = 0; i < 5; i++) { ... }
for i in range(5):
    print(f"{i}", end="")
# Output: 01234

# ---------------------------

# Countdown from 5 to 1
# In C: for (int i = 5; i > 0; i--)
for i in range(5, 0, -1):
    print(f"{i}", end="")
# Output: 54321

# ---------------------------

# Loop from 1 to 10 with a step of 2
# In C: for (int i = 1; i <= 10; i += 2)
for i in range(1, 11, 2):
    print(f"{i}", end="")
# Output: 13579

# ---------------------------

# Loop in list or string
# In C: for (int i = 0; str[i]; i++)
string = "this is string."
for i in string:
    print(f"{i}", end="") # in this loop print string Letter by letter
# Output: this is string.

# ---------------------------

list = [0, 7, 67, 57, 19, 52]
for i in list:
    print(f"{i}", end="") # in this loop print list element element
# Output: 0767571952
# ______________________________________________________________


# *****************************************************************************
# DATA TYPES & BUILT-IN DATA STRUCTURES
# *****************************************************************************

# 1.Basic Types
num			=	10			# Integer (int)
is_active	=	True		# boolean (bool)
decimal_num	=	5.9			# Floating point (float)
text_val	=	"Python"	# String (str)
# ______________________________________________________________

# 2.Built-in Data Structures
#---------------------------------------------------------------------------------------------------------------#
#PYTHON DATA STRUCTURES COMPARISON																				#
#---------------------------------------------------------------------------------------------------------------#
#	type	|	brackets	|	ordered	|		edit	|	duplicate	|				use						#
#-----------|---------------|-----------|---------------|---------------|---------------------------------------#
#	list	|		[ ]		|	index	|		yes		|	yes			|	General purpose / Dynamic Arrays	#
#	tuple	|		( )		|	index	|		no		|	yes			|	Coordinates / Fixed Data			#
#	set		|		{ }		|	no		|		yes*	|	no			|	Math operations / Unique items		#
#	dict	|		{ }		|	key		|		yes		|	keys: no	|	Key-Value pairs / Mapping			#
#---------------------------------------------------------------------------------------------------------------#
"""
	Note:
		+ If have duplicat same this {1, 1, 2, 3, 4, 2} in set, this is equale this {1, 2, 3, 4}.
        + Dict is ordered with keys & You cannot duplicate keys but can duplicate value of key.
"""

# 2-1.List
my_list = [12, True, "string", 10.872, [1, "inner_string"], ("tupel", 20)]

# 2-1-1. Print List
print(f"List: {my_list}") # Output: [12, True, "string", 10.872, [1, "inner_string"], ("tupel", 20)]

# 2-1-2. Accessing Elements (Index starts at 0)
print(f"First element: {my_list[0]}")

# 2-1-3. Accessing Nested Elements (Like 2D Arrays: my_list[row][col])
print(f"Nested item: {my_list[4][1]}")  # Output: inner_string

# 2-1-4. Negative Indexing (Starts from -1 at the end)
print(f"Last item: {my_list[-1]}")
print(f"Before last: {my_list[-2]}")

# ---------------------------

# 2-2. Tuple (Immutable - Cannot be changed)
my_tuple = (10, 20, "fixed", True, [1, 2])

# 2-2-1. Print Tuple
print(f"Tuple: {my_tuple}")

# 2-2-2. Accessing Elements (Same as List)
print(f"First element: {my_tuple[0]}")

# 2-2-3. Negative Indexing
print(f"Last item: {my_tuple[-1]}")
"""
	Note:
		You CANNOT do my_tuple[0] = 100 -> This will raise an Error.
"""

# ---------------------------

# 2-3. Set (Unordered & Unique elements)
my_set = {1, 2, 3, 3, "python"}

# 2-3-1. Print Set (Note: duplicate '3' is removed automatically)
print(f"Set: {my_set}") # Output: Random {3, 'python', 1, 2} or {2, "python", 3, 1} or ...

# 2-3-2. Checking Existence (No Indexing in Sets)
# In C: you need a loop to check. In Python:
print(f"Is 2 in set? {2 in my_set}") # Output: True

# 2-3-3. Adding/Removing
my_set.add(10)
my_set.remove(1)

# ---------------------------

# 2-4. Dictionary (Key-Value Pairs)
my_dict = {
    "name": "Adam",
    "nike name": "Chaos",
    "tags": ["python", "coding"]
}

# 2-4-1. Print Dictionary
print(f"Dict: {my_dict}")

# 2-4-2. Accessing Elements (Using Key instead of Index)
print(f"Name: {my_dict['name']}")

# 2-4-3. Accessing Nested List inside Dict
print(f"First tag: {my_dict['tags'][0]}")

# 2-4-4. Adding/Updating
my_dict["year"] = 2026  # Adding new key
my_dict["nike name"] = "adraji"  # Updating existing key


# *****************************************************************************
# COLLECT USER DATA
# *****************************************************************************

string = input("text")
# Input function print text, and takes data from the user in the form of string.

# ---------------------------

int("102")
# Int function to convert a text number or any basic data same float to an integer.

float(), str(), bool()
# Same function int.

"""
	Note:
		+ The int function does not accept any text that does not represent a integer number, such as '12a' or '10.1'
"""

# ---------------------------

# 1.String Data
name = input("Enter your name: ")

# 2.Int Data
age = int(input("Enter your age: "))

# 2.Float Data
weight = float(input("Enter your weight: "))


# -----------------------------------------------------------------------------
# TRY...EXCEPT: Handling runtime errors safely
# -----------------------------------------------------------------------------

# One Exceptions: Handling all types of errors in one exception
try:
    # Put code here that might cause an error
    number = int(input("Enter a number to divide 100: "))
    result = 100 / number
    print(f"Result is {result}")

except:
    # This code runs ONLY if an error occurs in the 'try' block
    print("Something went wrong! Please check your input.")

# ---------------------------

# One Exceptions: Handling One types of errors in one exception
try:
    # Put code here that might cause an error
    number = int(input("Enter a number to divide 100: "))
    result = 100 / number
    print(f"Result is {result}")

except ValueError:
    # This code runs ONLY if an value error occurs in the 'try' block
    # For exampel, user enter '1a', exit in 'try' block and enter except, but if user enter '0', program crush
    print("Something went wrong! Please check your input.")

# ---------------------------

# Multiple Exceptions: Dealing With Different Wrror Types

try:
    # Code that might fail
    number = int(input("Enter a number to divide 100: "))
    result = 100 / number
    print(f"Result is: {result}")

except ValueError:
    # Runs if user enters letters like '1a'
    print("Error: Please enter a valid numeric integer.")

except ZeroDivisionError:
    # Runs if user enters '0' - No more crash!
    print("Error: You cannot divide by zero.")

except Exception as error:
    # A 'catch-all' for any other unexpected errors
    # 'e' contains the error message (similar to strerror in C)
    print(f"An unexpected error occurred: {error}")


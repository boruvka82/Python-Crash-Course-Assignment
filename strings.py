#Question
#Try using the index method yourself now!

#Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious".

word = "supercalifragilisticexpialidocious"
print(word.index("x"))



#Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".

def student_grade(name, grade):
	return "{} received {}% on the exam".format(name,grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


# Formatting Strings Guide
# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""



#Skill Group 1
#Use a for loop to iterate through each letter of a string.

#Add a character to the front of a string.

#Add a character to the end of a string.

Use the .lower() string method to convert the case (uppercase/lowercase) of the letters within a string variable. This method is often used to eliminate cases as a factor when comparing two strings. For example, all lowercase “cat” is not equal to “Cat” because “Cat” contains an uppercase letter. To be able to compare the two strings to see if they are the same word, you can use the .lower() string method to remove capitalization as a factor in the string comparison.

# 1.This function accepts a given string and checks each character of 
# the string to see if it is a letter or not. If the character is a
# letter, that letter is added to the end of the string variable
# "forwards" and to the beginning of the string variable "backwards".
def mirrored_string(my_string):

    # Two variables are initialized as string data types using empty 
    # quotes. The variable "forwards" will hold the "my_string"
    # minus any character that is not a letter. The "backwards" 
    # variable will hold the same letters as "forwards", but in  
    # in reverse order.
    forwards = ""
    backwards = ""

    # The for loop iterates through each character of the "my_string"
    for character in my_string:

        # The if-statement checks if the character is not a space.
        if character.isalpha():

            # If True, the body of the loop adds the character to the
            # to the end of "forwards" and to the front of
            # "backwards". 
            forwards += character
            backwards = character + backwards

        # If False (meaning the character is not a letter), no action
        # is needed. This coding approach results prevents any 
        # non-alphabetical characters from being written to the
        # "forwards" and "backwards" variables. The for loop will 
        # restart until all characters in "my_string" have been
        # processed.
        
    # The final if-statement compares the "forwards" and "backwards"
    # strings to see if the letters are the same both forwards and
    # backwards. Since Python is case sensitive, the two strings will 
    # need to be converted to use the same case for this comparison. 
    if forwards.lower() == backwards.lower():
        return True
    return False
 
print(mirrored_string("12 Noon")) # Should be True
print(mirrored_string("Was it a car or cat I saw")) # Should be False
print(mirrored_string("'eve, Madam Eve")) # Should be True



#Skill Group 2
#Use the format() method, with {} placeholders for variable data, to create a new string.

#Use a formatting expression, like {:.2f}, to format a float variable and configure the number of decimal places to display for the float. 

# 2.This function converts measurement equivalents. Output is formatted 
# as, "x ounces equals y pounds", with y limited to 2 decimal places. 
def convert_weight(ounces):

    # Conversion formula: 1 pound = 16 ounces
    pounds = ounces/16 
    
    # The result is composed using the .format() method. There are two
    # placeholders in the string: the first is for the "ounces" 
    # variable and the second is for the "pounds" variable. The second
    # placeholder formats the float result of the conversion 
    # calculation to be limited to 2 decimal places.
    result = "{} ounces equals {:.2f} pounds".format(ounces,pounds)
    return result


print(convert_weight(12)) # Should be: 12 ounces equals 0.75 pounds
print(convert_weight(50.5)) # Should be: 50.5 ounces equals 3.16 pounds
print(convert_weight(16)) # Should be: 16 ounces equals 1.00 pounds



#Skill Group 3  

#Within the format() parameters, select characters at specific index [ ] positions from a variable string.  

#Use the format() method, with {} placeholders for variable data, to create a new string.
# 3.This function generates a username using the first 3 letters of a
# user’s last name plus their birth year. 
def username(last_name, birth_year):
    
    # The .format() method will use the first 3 letters at index 
    # positions [0,1,2] of the "last_name" variable for the first
    # {} placeholder. The second {} placeholder concatenates the user’s
    #  "birth_year" to that string to form a new string username.
    return("{}{}".format(last_name[0:3],birth_year))


print(username("Ivanov", "1985")) 
# Should display "Iva1985" 
print(username("Rodríguez", "2000")) 
# Should display "Rod2000" 
print(username("Deng", "1991")) 
# Should display "Den1991"

#String operations
len(string) Returns the length of the string
for character in string Iterates over each character in the string
if substring in string Checks whether the substring is part of the string
string[i] Accesses the character at index i of the string, starting at zero
string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.



#String methods
string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
string.count(substring) Returns the number of times substring is present in the string
string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 
Check out the official documentation for all available String methods.  

Official documentation for the format string syntax

# {:d} integer value
'{:d}'.format(10.5) → '10'

#Formatting expressions
Expr	Meaning	Example
{:d}	integer value	'{:d}'.format(10.5) → '10'
{:.2f}	floating point with that many decimals	'{:.2f}'.format(0.5) → '0.50'
{:.2s}	string with that many characters	'{:.2s}'.format('Python') → 'Py'
{:<6s}	string aligned to the left that many spaces	'{:<6s}'.format('Py') → 'Py    '
{:>6s}	string aligned to the right that many spaces	'{:>6s}'.format('Py') → '    Py'
{:^6s}	string centered in that many spaces	'{:^6s}'.format('Py') → '  Py  '
 Check out the official documentation for all available expressions.

#Old string formatting (Optional)
The format() method was introduced in Python 2.6. Before that, the % (modulo) operator could be used to get a similar result. While this method is no longer recommended for new code, you might come across it in someone else's code. This is what it looks like:
        "base string with %s placeholder" % variable


The % (modulo) operator returns a copy of the string where the placeholders indicated by %  followed by a formatting expression are replaced by the variables after the operator.
        "base string with %d and %d placeholders" % (value1, value2)

  To replace more than one value, the values need to be written between parentheses. The formatting expression needs to match the value type.
            "%(var1) %(var2)" % {var1:value1, var2:value2}


Variables can be replaced by name using a dictionary syntax (we’ll learn about dictionaries in an upcoming video).
            "Item: %s - Amount: %d - Price: %.2f" % (item, amount, price)


The formatting expressions are mostly the same as those of the format() method. 


Check out the official documentation for old string formatting.

#Formatted string literals (Optional)
This feature was added in Python 3.6 and isn’t used a lot yet. Again, it's included here in case you run into it in the future, but it's not needed for this or any upcoming courses.

A formatted string literal or f-string is a string that starts with 'f' or 'F' before the quotes. These strings might contain {} placeholders using expressions like the ones used for format method strings.

The important difference with the format method is that it takes the value of the variables from the current context, instead of taking the values from parameters.

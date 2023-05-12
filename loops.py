# Week 3 Graded Assessment


1.
Question 1
Fill in the blanks to print the even numbers from 2 to 12.

0 / 1 point
1234567
number = 2 # Initialize the variable 
while number <=12:
    if number%2 == 0: # Complete the while loop condition
        print(number, end=" ")
    number += 1 # Increment the variable

# Should print 2 4 6 8 10 12 
Reset
Incorrect
Please review the "What is a while loop?" video.

2.
Question 2
 Find and correct the error in the for loop below.  The loop should check each number from 1 to 5 and identify if the number is odd or even.  

1 / 1 point
12345678910111213
for number in range(1,6):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


# Should print:
# odd
# even

Reset
Correct
Correct

3.
Question 3
Fill in the blanks to complete the “factorial” function. This function will accept an integer variable “n” through the function parameters and produce the factorials of this number (by multiplying this value by every number less than the original number [n*(n-1)], excluding 0).  To do this, the function should:

accept an integer variable “n” through the function parameters;

initialize a variable “result” to the value of the “n” variable;

iterate over the values of “n” using a while loop until “n” is equal to 0;

starting at n-1, multiply the result by the current “n” value;

decrement “n” by -1.

 For example, factorial 3 would return the value of 3*2*1, which would be 6.

1 / 1 point
12345678910111213
def factorial(n):
    result = n
    start = n
    n -= 1
    while n>0: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n-=1 # Decrement the appropriate variable by -1
    return result



Reset
Correct
Correct

4.
Question 4
Fill in the blanks to complete the “sequence” function. This function should print a sequence of numbers in descending order, from the given "high" variable to the given "low" variable.  The range should make the loop run two times. Complete the range sequences in the nested loops so that the “sequence(1, 3)” function call prints the following:

3, 2, 1

3, 2, 1

1 / 1 point
1234567891011121314151617
def sequence(low, high):
    # Complete the outer loop range to make the loop run twice
    # to create two rows
    for x in range(2): 
        # Complete the inner loop range to print the given variable
        # numbers starting from "high" to "low" 
        # Hint: To decrement a range parameter, use negative numbers
        for y in range(high, low -1, -1): 
            if y == low:
                # Don’t print a comma after the last item

Reset
Correct
Correct

5.
Question 5
Fill in the blanks to complete the “counter” function. This function should count down from the “start” to “stop” variables when “start” is bigger than “stop”. Otherwise, it should count up from “start” to “stop”. Complete the code so that a function call like “counter(3, 1)” will return “Counting down: 3, 2, 1” and “counter(2, 5)” will return “Counting up: 2, 3, 4, 5”.

1 / 1 point
123456789101112131415161718192021
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop: # Complete the while loop
            return_string = return_string + str(start) # Add the numbers to the "return_string"
            if start > stop:
                return_string += ","
            start -= 1 # Increment the appropriate variable
    else:
        return_string = "Counting up: "

Reset
Correct
Correct

6.
Question 6
Fill in the blanks to complete the “all_numbers” function. This function should return a space-separated string of all numbers, from the starting   “minimum” variable  up to and including the “maximum” variable that's passed into the function. Complete the for loop so that a function call like “all_numbers(3,6)” will return the numbers “3 4 5 6”.  

1 / 1 point
12345678910111213141516171819202122
def all_numbers(minimum, maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # numbers up to and including the "maximum" value.
    for number in range(minimum, maximum+1):

        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.

Reset
Correct
Correct

7.
Question 7
What happens when the Python interpreter executes a loop where a variable used inside the loop is not initialized?

1 / 1 point

Will produce a NameError stating the variable is not defined


The variable will be auto-assigned a default value of 0


Nothing will happen 


Will produce a TypeError 

Correct
8.
Question 8
What is the final value of “x” at the end of this for loop? Your answer should be only one number.

12
for x in range(1, 10, 3):
    print(x)

1 / 1 point
7
Correct
9.
Question 9
What is the final value of "y" at the end of the following nested loop code? Your answer should be only one number.

123
for x in range(10):
    for y in range(x):
        print(y)

1 / 1 point
8
Correct
10.
Question 10
The following code causes an infinite loop. Can you figure out what is incorrect?

123456
def test_code(num):
  x = num
  while x % 2 == 0:
    x = x / 2

test_code(0)

1 / 1 point

The modulo operator is used incorrectly


Missing an else statement


When called with 0, it triggers an infinite loop


Missing the continue keyword

Correct












# QUIZ

1.
#Question 1
#In Python, what do while loops do?  

#while loops tell the computer to repeatedly execute a set of instructions while a condition is true.  

#Question 2
#Which techniques can prevent an infinite while loop? Select all that apply. 

Change the value of a variable used in the while condition

Correct
Correct. If a numeric variable is used to control the iterations of a while condition, that variable must eventually change to a value that makes the while condition False, otherwise the while loop will keep executing indefinitely.

Use the break keyword

Correct
Correct. The break keyword can stop a while loop. It is often used in the body of a nested if-else conditional statement inside of a while loop. 

#Question 3
 #The following code contains an infinite loop, meaning the Python interpreter does not know when to exit the loop once the task is complete. To solve the problem, you will need to:  
  #Find the error in the code
#Fix the while loop so there is an exit condition

def is_power_of_two(number):  TO BE DONE!!!!!
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  while number % 2 == 0:
    number = number / 2
  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
    if number == 1:
      return True
  return False

# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False


Incorrect
Timed out after 5

#Question 4
#Fill in the blanks to complete the while loop so that it returns the sum of all the divisors of a number, without including the number itself. As a reminder, a divisor is a number that divides into another without a remainder. To do this, you will need to:
#Initialize the "divisor" and "total" variables with starting values
#Complete the while loop condition
#Increment the "divisor" variable inside the while loop
#Complete the return statement

# Fill in the blanks so that the while loop continues to run while the
# "divisor" variable is less than the "number" parameter.

def sum_divisors(number):
# Initialize the appropriate variables
  divisor = 1
  total = 0

  # Avoid dividing by 0 and negative numbers 
  # in the while loop by exiting the function
  # if "number" is less than one
  if number < 1:
    return 0 

  # Complete the while loop
  while divisor < number:
    if number % divisor == 0:
      total += divisor
    # Increment the correct variable
    divisor += 1

  # Return the correct variable 
  return total


print(sum_divisors(0)) # Should print 0
print(sum_divisors(3)) # Should print 1
# 1
print(sum_divisors(36)) # Should print 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should print 1+2+3+6+17+34+51
# 114


#Question 5
#Fill in the blanks to complete the function, which should output a multiplication table. The function accepts a variable “number” through its parameters. This “number” variable should be multiplied by the numbers 1 through 5, and printed in a format similar to “1x6=6” (“number” x “multiplier” = “result”). The code should also limit the “result” to not exceed 25. To satisfy these conditions, you will need to:

#Initialize the “multiplier" variable with the starting value
#Complete the while loop condition
#Add an exit point for the loop
#Increment the “multiplier" variable inside the while loop

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier in range(1,6):
        result = number * multiplier 
        if  result > 25 :
            # Enter the action to take if the result is greater than 25
            return False
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3) 
# Should print: 
# 3x1=3 
# 3x2=6 
# 3x3=9 
# 3x4=12 
# 3x5=15

multiplication_table(5) 
# Should print: 
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25

multiplication_table(8) 
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24




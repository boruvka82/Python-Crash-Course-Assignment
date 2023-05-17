1.
Question 1
The format of the input variable “address_string” is: numeric house number, followed by the street name which may contain numbers and could be several words long (e.g., "123 Main Street", "1001 1st Ave", or "55 North Center Drive"). 

Complete the string methods needed in this function so that input like "123 Main Street" will produce the output "House number 123 on a street named Main Street". This function should:

accept a string through the parameters of the function;

separate the address string into new strings: house_number and street_name; 

return the variables in the string format: "House number X on a street named Y". 

def format_address(address_string):


    house_number = ""
    street_name = ""


    # Separate the house number from the street name.
    address_parts = address_string.split(" ")
    
    for address_part in address_parts:
       # Complete the if-statement with a string method.  
       if address_part.isnumeric():
         house_number = address_part
       else:
         street_name += address_part + " "
    # Remove the extra space at the end of the last "street_name".
    street_name = street_name.rstrip()
 
    # Use a string method to return the required formatted string.
    return (f"House number {house_number} on a street named {street_name}")


print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"


print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"


print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"



Question 2
Complete the for loop and string method needed in this function so that a function call like "alpha_length("This has 1 number in it")" will return the output "17". This function should:

accept a string through the parameters of the function;

iterate over the characters in the string;

determine if each character is a letter (counting only alphabetic characters; numbers, punctuation, and spaces should be ignored);

increment the counter;

return the count of letters in the string.

def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for character in string : 
        # Complete the if-statement using a string method. 
        if character.isalpha():
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21



.
Question 3
Consider the following scenario about using Python lists: 

A professor gave his two assistants, Aniyah and Imani, the task of keeping an attendance list of students in the order they arrived in the classroom. Aniyah was the first one to note which students arrived, and then Imani took over. After class, they each entered their lists into the computer and emailed them to the professor. The professor wants to combine the two lists into one and sort it in alphabetical order. 

Complete the code by combining the two lists into one and then sorting the new list. This function should:

accept two lists through the function’s parameters;,

combine the two lists;

sort the combined list in alphabetical order;

return the new list. 

def alphabetize_lists(list1, list2):


  new_list = [] # Initialize a new list.
  combined = list1 + list2 # Combine the lists.
  combined.sort() # Sort the combined lists.
  new_list = combined # Assign the combined lists to the "new_list".
  return new_list


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']



4.
Fill in the blank to complete the “even_numbers” function. This function should use a list comprehension to create a list of even numbers using a conditional if statement with the modulo operator to test for numbers evenly divisible by 2. The function receives two variables and should return the list of even numbers that occur between the “first” and “last” variables exclusively (meaning don’t modify the default behavior of the range to exclude the “end” value in the range). For example, even_numbers(2, 7) should return [2, 4, 6].  
def even_numbers(first, last):
  return [ x for x in range(first,last) if x % 2 == 0  ]


print(even_numbers(4, 14)) # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))  # Should print [2, 4, 6]



.
Question 5
Fill in the blanks to complete the “countries” function. This function accepts a dictionary containing a list of continents (keys) and several countries from each continent (values).  For each continent, format a string to print the names of the countries only. The values for each key should appear on their own line.

def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.
    for continent, countries in countries_dict.items():
        # Use a string method to format the required string.
        result += str(countries) + '\n'
    return result

print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))

# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']



6.
Question 6
Consider the following scenario about using Python dictionaries: 

Tessa and Rick are hosting a party. Together, they sent out invitations, and collected the responses in a dictionary, with names of their friends and the number of guests each friend will be bringing. 

Complete the function so that the “check_guests” function retrieves the number of guests (value)  the specified friend “guest” (key) is bringing. This function should:

accept a dictionary “guest_list” and a key “guest” variable passed through the function parameters;

print the values associated with the key variable.

def check_guests(guest_list, guest):
  return guest_list[guest] # Return the value for the given key


guest_list = { "Adam":3, "Camila":3, "David":5, "Jamal":3, "Charley":2, "Titus":1, "Raj":6, "Noemi":1, "Sakira":3, "Chidi":5}


print(check_guests(guest_list, "Adam")) # Should print 3
print(check_guests(guest_list, "Sakira")) # Should print 3
print(check_guests(guest_list, "Charley")) # Should print 2




Question 7
Complete the function so that input like "This is a sentence." will return a dictionary that holds the count of each letter that occurs in the string: {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}. This function should:

accept a string “text” variable through the function’s parameters;

iterate over each character the input string to count the frequency of each letter found, (only letters should be counted, do not count blank spaces, numbers, or punctuation; keep in mind that Python is case sensitive);

populate the new dictionary with the letters as keys, ensuring each key is unique, and assign the value for each key with the count of that letter;

return the new dictionary.


def count_letters(text):
  # Initialize a new dictionary.
  dictionary = {} 
  # Complete the for loop to iterate through each "text" character and 
  # use a string method to ensure all letters are lowercase.
  for letter in text.lower():   
    # Complete the if-statement using a string method to check if the
    # character is a letter.
    if letter.isalpha(): 
      # Complete the if-statement using a logical operator to check if 
      # the letter is not already in the dictionary.
      if letter in dictionary: 
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
           dictionary[letter] += 1  
      # Use a dictionary operation to increment the letter count value 
      # for the existing key.
      else:  
        dictionary[letter] = 1 # Increment the letter counter. 
  return dictionary

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

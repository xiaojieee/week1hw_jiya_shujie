# var = input("please enter a value: ")
# to output a prompt to the console and getting a reply
# the variable var is a reference to that reply, and it is a string in this case

var = input("please enter a value: ")
print('This is the value: ', var)
# printing out the input of var

upper_case = var.upper()
# upper_case is my new variable that convert var to upper cases
# .upper() returns a string where all the characters are in upper case
# symbols and numbers are ignored
print('This is in upper case: ', upper_case)


numbers_of_characters_in_var = len(var)
print('The number of characters in the value: ', numbers_of_characters_in_var)
# len is a built-in function that calculates the number of characters in a string

print('The number of characters in the value: ', len(var))
# shortened to one line

does_it_contain_numeric_characters = var.isdecimal()
print('It is all decimal characters: ', does_it_contain_numeric_characters)
# isdecimal() returns True if all characters in the string are decimals
# if the value contains characters or floating numbers it will return False
# And it must not be empty

print('It is all decimal characters: ', var.isdecimal())
# shortened to one line


print('It is all digits: ', var.isdigit())
# isdigit() returns True if all characters in string are integers and no spaces

print('It is all numeric: ', var.isnumeric())
# isnumeric() works with fractions, superscript and Roman numerals

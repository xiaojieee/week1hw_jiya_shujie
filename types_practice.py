# Shujie's Name Dictionary
first_name = 'shujie'
last_name = 'zhu'
# my two variables are "first_name" and "last_name"
# putting quotes around the word makes it a string

full_name = first_name + ' ' + last_name
# to put a space in the output, it will literally need to be a space in quotes
print(full_name)

# list - transfer the variables into a list
name_list = [first_name, last_name]
print(name_list)
# lists are in square brackets

# dictionary - transfer the variables into a dictionary
name_dictionary = {'first': 'shujie', 'last': 'zhu'}
print(name_dictionary)
# dictionary are in braces, and are presented in key: value pairs


# EXERCISE 9, Part 1
# Two Variables below one containing my first name and the other my last
first_name = 'Jiya'
last_name = 'Bharti'
# the print function and concatenation allows for the display with a space
print(first_name + ' ' + last_name)

# Now I am adding the variables into a list
fullname_list = [first_name + ' ' + last_name]
print(fullname_list)


# Jiya's Name Dictionary
                                    # DICTIONARY CREATION

# creating a list using variables and keys
# the keys and their corresponding values
keys = ['first','last']
values = [first_name, last_name]

# Creating a dictionary using a loop
my_dict = {}
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]
#     I have no clue what the above does tbh, I tried figuring it out..ASKKKK!!!!!!!

# Displaying the dictionary
print(my_dict)

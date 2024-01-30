                                    # EXERCISE 9, Part 1
# Two Variables below one containing my first name and the other my last
first_name = 'Jiya'
last_name = 'Bharti'
# the print function and concatenation allows for the display with a space
print(first_name + ' ' + last_name)

# Now I am adding the variables into a list
fullname_list = [first_name + ' ' + last_name]
print(fullname_list)

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


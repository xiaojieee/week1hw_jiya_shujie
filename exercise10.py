import sys, glob, os
# sys is system-specific parameters and functions
# glob finds all path names matching a specific pattern
# os - a portable way of using operating system dependent functionality

# Get the directory name

if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
# == is an equality operator
# environ['HOME'] or environ['HOMEPATH']  is the pathname of the home directory
# HOMEPATH is for windows, HOME is for Linux

print(sys.platform)
# line 15 show sys platform is in fact win32
print(hdir)
# my variable hdir shows the name of my home directory which is \user\sjzhu

# Construct a portable wildcard pattern
# the '*' is the wild card pattern in this situation
# it is used to matches any sequence of characters
pattern = os.path.join(hdir, '*')
# os.path.join function is used to join one or more path components
# the '*' here means all

# TODO: Use the glob.glob() function to obtain the list of filenames
# glob.glob() is used to find all directories/files that match a certain pattern

list_file_name = glob.glob(pattern)
# listing all the files that match the 'pattern'
print(list_file_name)

# TODO: use os.path.getsize to find each file's size

file_size = os.path.getsize(hdir)
print(file_size)
# the files total size

for hdir in list_file_name:
    size = os.path.getsize(hdir)
    print(f"{hdir}: {size}")
# 'for' loop iterate through a sequence
# loop variable holds a copy of each element in turn
# the f-string allows embed expressions inside string literals
# hdir and size are the two variables I want to display side by side

# TODO: Add a test to only display files that are not zero length

    if size > 0:
        print(f"{hdir}: {size}")
# if size is bigger than zero print the file and its size
# remember to indent for it to work
# doesn't work check back on this

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

    if size > 0:
        file_name = os.path.basename(hdir)
        print(f"{file_name}: {size}")


# Exercise 10 Q2 create a bank pin program

print("Welcome to the bank!")
correct_pin = "1234"
# the pin have to be in a string, the input function is treated as string
attempts = 3

while attempts > 0:
    supplied_pin = input("Enter your PIN:")

# while there's attempts left print the "enter your pin"

    if supplied_pin == correct_pin:
        print("Correct pin!")
        break
    #   break is used to break the loop if the answer is correct
    else:
        attempts -= 1
        print(f"Wrong pin, {attempts} attempts left")
    #   -= means subtract AND: attempts = attempts - 1

if attempts == 0:
    print("You have entered the wrong pin 3 times, no attempts left")
    # if there's no attempts left print the end message

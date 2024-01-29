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
#HOMEPATH is for windows, HOME is for Linux

print(sys.platform)
# line 15 show sys platform is in fact win32
print(hdir)
# my variable hdir shows the name of my home directory which is \user\sjzhu

# Construct a portable wildcard pattern

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



# TODO: Add a test to only display files that are not zero length

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

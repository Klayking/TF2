# The built-in function `open` opens a file and returns a file object.

# Read mode opens a file for reading only.
herp = input()

while (herp <> "exit")
	
try:
    f = open("Roster.txt", "r")
    try:
				string= f.read()
				print(string)
    finally:
        f.close()
				print("Text File found")
except IOError:
    pass


# Write mode creates a new file or overwrites the existing content of the file.
# Write mode will _always_ destroy the existing contents of a file.
try:
    # This will create a new file or **overwrite an existing file**.
		clan = input()
    f = open(clan + ".txt", "w")
    try:
        f.write('blah') # Write a string to a file
        f.writelines(lines) # Write a sequence of strings to a file
    finally:
        f.close()
except IOError:
    pass

# Append mode adds to the existing content, e.g. for keeping a log file. Append
# mode will _never_ harm the existing contents of a file.
try:
    # This tries to open an existing file but creates a new file if necessary.
    logfile = open("log.txt", "a")
    try:
        logfile.write('log log log')
    finally:
        logfile.close()
except IOError:
    pass

# There is also r+ (read and write) mode.
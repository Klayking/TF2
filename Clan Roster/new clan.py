print("Clan Name:")
clan = input()

f = open(clan + ".txt", "w")
print("Does clan have url: y/n")
url = input()

if url=="y":
  print("Clan Group URL")
  groupurl = input()
  ClanLine = "[i][b][url=" + groupurl + "][noparse]" + clan + "[/noparse][/url][/b][/i]"
else:
  ClanLine = "[i][b][url=" + groupurl + "][noparse]" + clan + "[/noparse][/url][/b][/i]"


print("Manager:")
manager = input()

print("Manager URL:")
managerurl = input()

print("Do you have more than one Manager: y/n")
moremanager = input()
if moremanager = "y"

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
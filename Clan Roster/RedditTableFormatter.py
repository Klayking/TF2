file = open("fixedconditions.txt", 'w')

with open("conditions.txt") as f:
    content = f.readlines()
		
for line in content:
	start = True
	eos = False
	out = ""
	starter = ""
	for c in line:
		if start:
			if c == " ":
				start = False
				eos = True
			else:
				starter += c
		if eos:
			eos = False
			out = "|  " + starter + "|"
		if (not eos) and (not start) and (c != "\n"):
			out += c
	out += "|\n"
	file.write(out)
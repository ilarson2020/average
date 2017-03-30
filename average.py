f = open("file.txt", "r")

sum = 0

average = 0

readfile = f.readlines
for line in f:
	line = int(line)
	sum += line
print(sum)
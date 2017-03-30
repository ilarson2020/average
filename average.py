f = open("file.txt", "r")

sum = 0

average = 0

readfile = f.readlines()
f.seek(0)
for line in f:
	line = int(line)
	sum += line
print(sum)
average = sum / len(readfile)
print(average)
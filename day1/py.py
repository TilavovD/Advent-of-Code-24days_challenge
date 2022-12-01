from input import data
data = data.split("\n")

for i in data:
	if i == "":
		if max < sum:
			max = sum
		sum = 0	
	else:
		sum += int(i)
if max < sum:
	max = sum
print(max)
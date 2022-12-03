from input import data

data = data.split()

sum = 0

for row in data:
	for char_index in range(len(row)//2):
		if row[char_index] in row[len(row)//2:]:
			if ord(row[char_index]) > 90:
				sum += -96 + ord(row[char_index])
			else:
				sum += -38 + ord(row[char_index])
			print(row[char_index])
			break
			
print(sum)
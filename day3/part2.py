from input import data

data = data.split()

sum = 0

for row_index in range(0, len(data), 3):
	for char_index in range(len(data[row_index])):
		if data[row_index][char_index] in data[row_index+1] and data[row_index][char_index] in data[row_index+2]:
			if ord(data[row_index][char_index]) > 90:
				sum += -96 + ord(data[row_index][char_index])
			else:
				sum += -38 + ord(data[row_index][char_index])
			print(data[row_index][char_index])
			break
			
print(sum)
from input import data
data = data.split("\n")
sum = 0
max = 0
arr = []
for i in data:
	if i == "":
		if max < sum:
			max = sum
			if len(arr) < 3:
				arr.append(max)
				print(arr)
			else:
				min_arr = min(arr)
				min_index = arr.index(min_arr)
				arr[min_index] = max
		sum = 0
		
	else:
		sum += int(i)
if max<sum:
	max = sum
print(arr[0]+arr[1]+arr[2])

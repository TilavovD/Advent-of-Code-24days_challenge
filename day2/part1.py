from input import data
data = data.split()
data_dict = {"AX":0, "AY":0, "AZ":0, "BX":0, "BY":0, "BZ":0, "CX":0, "CY":0, "CZ":0}

for i in range(0, len(data), 2):
	row = f"{data[i]}{data[i+1]}"
	data_dict[row]+=1

result = data_dict["AX"] * (3 + 1) + data_dict["BX"] * (1+0) + data_dict["CX"] * (1 + 6)

result += data_dict["AY"] * (2 + 6) + data_dict["BY"] * (2+3) + data_dict["CY"] * (2 + 0)

result += data_dict["AZ"] * (3 + 0) + data_dict["BZ"] * (3+6) + data_dict["CZ"] * (3 + 3)

print(result)

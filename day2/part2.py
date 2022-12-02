from input import data
data = data.split()
data_dict = {"AX":0, "AY":0, "AZ":0, "BX":0, "BY":0, "BZ":0, "CX":0, "CY":0, "CZ":0}

for i in range(0, len(data), 2):
	row = f"{data[i]}{data[i+1]}"
	data_dict[row]+=1

result = data_dict["AX"] * (0 + 3) + data_dict["BX"] * (0+1) + data_dict["CX"] * (0 + 2)

result += data_dict["AY"] * (3 + 1) + data_dict["BY"] * (3+2) + data_dict["CY"] * (3 + 3)

result += data_dict["AZ"] * (6 + 2) + data_dict["BZ"] * (6+3) + data_dict["CZ"] * (6 + 1)

print(result)

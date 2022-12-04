from input import data
data = data.split()

def record_splitter(record):
	record = record.split(",")
	record1 = record[0]
	record2 = record[1]
	record1_start = record1.split("-")[0]
	record1_end = record1.split("-")[1]
	record2_start = record2.split("-")[0]
	record2_end = record2.split("-")[1]
	return record1_start, record1_end, record2_start, record2_end

count = 0
for row_index in range(len(data)):

	record1_start, record1_end, record2_start, record2_end = record_splitter(data[row_index])

	if int(record1_start) <= int(record2_start) and int(record1_end) >= int(record2_end) or int(record1_start) >= int(record2_start) and int(record1_end) <= int(record2_end):
		print(record1_start, record1_end, record2_start, record2_end)
		count += 1

print(count)
# Cách 1
import csv
def convert_medv(medv):
    if float(medv) < 20:
        return "Thấp"
    else:
        return "Cao"

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    data = list(reader)

for row in data:
    row[-1] = convert_medv(row[-1])
    
with open('modified_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print("Modified data has been written to modified_data.csv")


#Cách 2
import csv
def convert_medv(medv):
    if float(medv) < 20:
        return "Thấp"
    else:
        return "Cao"

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    data = list(reader)

for row in data:
    row[-1] = convert_medv(row[-1])
    
with open('modified_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("Modified data has been written to modified_data.csv")

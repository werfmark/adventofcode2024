import os

def read_input_data(file_path):
    jagged_array = []
    with open(file_path, 'r') as file:
        for line in file:
            numbers = list(map(int, line.split()))
            jagged_array.append(numbers)
    return jagged_array

def is_safe(row):
    return all(row[i+1] - row[i] > 0 and row[i+1] - row[i] < 4 for i in range(len(row) - 1)) \
        or all(row[i+1] - row[i] < 0 and row[i+1] - row[i] > -4 for i in range(len(row) - 1))

script_dir = os.path.dirname(__file__)
input_file_path = os.path.join(script_dir, 'inputData.txt')
jagged_array = read_input_data(input_file_path)


#part1
total_safe = 0

for row in jagged_array:
    if is_safe(row):
        total_safe += 1
    
print(total_safe)

#part2
total_safe_2 = 0

for row in jagged_array:
    if is_safe(row):
        total_safe_2 += 1
        continue
    for i in range(len(row)):
        if is_safe(row[:i] + row[i+1:]):
            total_safe_2 += 1
            break

print (total_safe_2)
import os

script_dir = os.path.dirname(__file__)
input_file_path = os.path.join(script_dir, 'inputData.txt')

list1 = []
list2 = []

with open(input_file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        list1.append(int(line.strip().split()[0]))
        list2.append(int(line.strip().split()[1]))

# work inprogress, srot lists and substract pairwise

list1.sort()
list2.sort()

total_difference = 0
for a, b in zip(list1, list2):
    total_difference += abs(a - b)

print(total_difference)



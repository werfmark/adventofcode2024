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

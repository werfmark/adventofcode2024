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


#part1
list1.sort()
list2.sort()

total_difference = sum(abs(a - b) for a, b in zip(list1, list2))
print(total_difference)

#part2
similarity_score = sum(a * list2.count(a) for a in list1)
print(similarity_score)











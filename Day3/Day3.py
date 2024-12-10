import re

data = open("Day3\inputData.txt").read()

#part1
pattern = re.compile(r'mul\((\d+),(\d+)\)')
matches = pattern.findall(data)

total = 0
for match in matches:
    total += int(match[0]) * int(match[1])

print(total)

#part2
pattern2 = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
matches = pattern2.findall(data)

total_2 = 0
flag = True
for match in matches:
    if match == "do()":
        flag = True
    elif match == "don't()":
        flag = False
    elif flag:
        x,y = map(int, match[4:-1].split(","))
        total_2 += x * y

print(total_2)



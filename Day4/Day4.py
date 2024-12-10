test_data = open("Day4\inputData.txt").readlines()

# test_data = [
#     "MMMSXXMASM",
#     "MSAMXMSMSA",
#     "AMXSXMAAMM",
#     "MSAMASMSMX",
#     "XMASAMXAMM",
#     "XXAMMXXAMA",
#     "SMSMSASXSS",
#     "SAXAMASAAA",
#     "MAMMMXMMMM",
#     "MXMXAXMASX"
# ]

#pad with empty to prevent out of bounds
test_data = ["OOO" + line + "OOO" for line in test_data]
test_data = ["O" * len(test_data[0])] * 3 + test_data + ["O" * len(test_data[0])] * 3

# Part 1
count_xmas = 0

width = len(test_data)

for i in range(3, width - 3):
    for j in range(3, width - 3):
        if test_data[i][j] == "X":
            #EAST
            if test_data[i][j+1] == "M" and test_data[i][j+2] == "A" and test_data[i][j+3] == "S":
                count_xmas += 1
            #SOUTHEAST
            if test_data[i+1][j+1] == "M" and test_data[i+2][j+2] == "A" and test_data[i+3][j+3] == "S":
                count_xmas += 1
            #SOUTH
            if test_data[i+1][j] == "M" and test_data[i+2][j] == "A" and test_data[i+3][j] == "S":
                count_xmas += 1
            #SOUTHWEST
            if test_data[i+1][j-1] == "M" and test_data[i+2][j-2] == "A" and test_data[i+3][j-3] == "S":
                count_xmas += 1
            #WEST
            if test_data[i][j-1] == "M" and test_data[i][j-2] == "A" and test_data[i][j-3] == "S":
                count_xmas += 1
            #NORTHWEST
            if test_data[i-1][j-1] == "M" and test_data[i-2][j-2] == "A" and test_data[i-3][j-3] == "S":
                count_xmas += 1
            #NORTH
            if test_data[i-1][j] == "M" and test_data[i-2][j] == "A" and test_data[i-3][j] == "S":
                count_xmas += 1
            #NORTHEAST
            if test_data[i-1][j+1] == "M" and test_data[i-2][j+2] == "A" and test_data[i-3][j+3] == "S":
                count_xmas += 1

print(count_xmas)


#part2
count_mas_cross = 0

def is_mas_cross(i, j, NWchar, NEchar, SWchar, SEchar):
    return test_data[i-1][j-1] == NWchar and test_data[i-1][j+1] == NEchar and test_data[i+1][j-1] == SWchar and test_data[i+1][j+1] == SEchar

for i in range(4, width - 4):
    for j in range(4, width - 4):
        if test_data[i][j] == "A":
            #SOUTHEAST
            if is_mas_cross(i, j, "M", "M", "S", "S"):
                count_mas_cross += 1
            #SOUTHWEST
            elif is_mas_cross(i, j, "S", "M", "S", "M"):
                count_mas_cross += 1
            #NORTHWEST
            elif is_mas_cross(i, j, "S", "S", "M", "M"):
                count_mas_cross += 1
            #NORTHEAST
            elif is_mas_cross(i, j, "M", "S", "M", "S"):
                count_mas_cross += 1

print(count_mas_cross)
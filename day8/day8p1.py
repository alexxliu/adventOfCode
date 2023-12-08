f = open("adventOfCode\day8\day8input.txt", "r")

lines = f.readlines()

instructions = lines[0][:-1]

leftMap = {}
rightMap = {}
for i in range(2, len(lines)):
    key = lines[i][0:3]
    left = lines[i][7:10]
    right = lines[i][12:15]

    leftMap[key] = left
    rightMap[key] = right

cur = "AAA"
count = 0
flag = True

while flag:
    for c in instructions:
        if c == "L":
            cur = leftMap[cur]
        elif c == "R":
            cur = rightMap[cur]
        
        count += 1

        if cur == "ZZZ":
            print(count)
            flag = False

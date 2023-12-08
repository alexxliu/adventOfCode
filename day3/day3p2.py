from collections import defaultdict

f = open("day3/day3input.txt", "r")

lines = f.readlines()

res = 0

adjacent = ((0,1), (0,-1), (1,0), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1))

symbolLoc = set()
# key = (x, y) : value = [num1, num2, ...]
gears = defaultdict(list)

# find all gears
for r in range(len(lines)):
    for c in range(len(lines[r])):

        if lines[r][c] == "*":
            symbolLoc.add((r, c))

# find each number and scan for adjacent gears. add the number to the map 
for r in range(len(lines)):
    c = 0
    curNum = 0
    savedLoc = []
    while c < len(lines[r]):
        while lines[r][c].isnumeric():
            curNum *= 10
            curNum += int(lines[r][c])
            for dx, dy in adjacent:
                if (r+dx, c+dy) in symbolLoc:
                    savedLoc.append((r+dx,c+dy))
            
            c += 1
        
        for x, y in savedLoc:
            gears((x, y)).append(curNum)

        savedLoc = []
        curNum = 0
        c += 1

for val in gears.values():
    if len(val) == 2:
        res += val[0] * val[1]

print(res)
            


            

            
        


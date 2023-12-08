f = open("day3/day3input.txt", "r")

lines = f.readlines()

res = 0

adjacent = ((0,1), (0,-1), (1,0), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1))

symbolLoc = set()

# find all symbols
for r in range(len(lines)):
    for c in range(len(lines[r])):

        if lines[r][c] != "." and lines[r][c] != "\n" and not lines[r][c].isalnum():
            symbolLoc.add((r, c))

# find each number and scan for adjacent symbols
for r in range(len(lines)):
    c = 0
    curNum = 0
    isPartNum = False
    while c < len(lines[r]):
        while lines[r][c].isnumeric():
            curNum *= 10
            curNum += int(lines[r][c])
            for dx, dy in adjacent:
                if (r+dx, c+dy) in symbolLoc:
                    isPartNum = True
            
            c += 1
        
        if isPartNum:
            res += curNum

        curNum = 0
        isPartNum = False
        c += 1

print(res)
            


            

            
        


f = open("day1/day1input.txt", "r")

lines = f.readlines()

sum = 0
threeLetters = {"one" : 1, "two" : 2, "six" : 6}
fourLetters = {"four" : 4, "five" : 5, "nine" : 9}
fiveLetters = {"three" : 3, "seven" : 7, "eight" : 8}

for line in lines:
    oldSum = sum

    for l in range(len(line)):
        if line[l].isnumeric():
            sum += int(line[l]) * 10
            break
        elif l < len(line)-3 and line[l:l+3] in threeLetters:
            sum += threeLetters[line[l:l+3]] * 10
            break
        elif l < len(line)-4 and line[l:l+4] in fourLetters:
            sum += fourLetters[line[l:l+4]] * 10
            break
        elif l < len(line)-5 and line[l:l+5] in fiveLetters:
            sum += fiveLetters[line[l:l+5]] * 10
            break

    for r in range(len(line)-1, -1, -1):
        if line[r].isnumeric():
            sum += int(line[r])
            break
        elif r >= 3 and line[r-3:r] in threeLetters:
            sum += threeLetters[line[r-3:r]]
            break
        elif r >= 4 and line[r-4:r] in fourLetters:
            sum += fourLetters[line[r-4:r]]
            break
        elif r >= 5 and line[r-5:r] in fiveLetters:
            sum += fiveLetters[line[r-5:r]]
            break

    print(sum - oldSum)

f.close()

print(sum)
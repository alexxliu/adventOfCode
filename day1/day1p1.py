f = open("day1/day1input.txt", "r")

lines = f.readlines()

sum = 0
threeLetters = {"one" : 1, "two" : 2, "six" : 6}
fourLetters = {"four" : 4, "five" : 5, "nine" : 9}
fiveLetters = {"three" : 3, "seven" : 7, "eight" : 8}

for line in lines:
    l, r = 0, len(line)-1

    while not line[l].isnumeric():
        l += 1

    while not line[r].isnumeric():
        r -= 1
            
    sum += int(line[l])*10 + int(line[r])

f.close()

print(sum)
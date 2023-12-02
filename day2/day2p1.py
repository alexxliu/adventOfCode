f = open("day2/day2input.txt", "r")

lines = f.readlines()

red = 12
green = 13
blue = 14

res = 0

for line in lines:
    games = line.split(": ")

    gameNum = games[0]
    gameNum = gameNum.split(" ")
    gameNum = gameNum[1]

    games = games[1]
    games = games.split("; ")
    flag = True
    for game in games:
        counts = game.split(", ")
        for c in counts:
            count, color = c.split(" ")
            if "red" in color and int(count) > red:
                flag = False
            if "blue" in color and int(count) > blue:
                flag = False
            if "green" in color and int(count) > green:
                flag = False
    if flag:
        res += int(gameNum)

print(res)
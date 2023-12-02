f = open("day2/day2input.txt", "r")

lines = f.readlines()

res = 0

for line in lines:
    games = line.split(": ")

    gameNum = games[0]
    gameNum = gameNum.split(" ")
    gameNum = gameNum[1]

    games = games[1]
    games = games.split("; ")
    r = 0
    b = 0
    g = 0
    for game in games:
        counts = game.split(", ")
        for c in counts:
            count, color = c.split(" ")
            if "red" in color:
                r = max(r, int(count))
            if "blue" in color:
                b = max(b, int(count))
            if "green" in color:
                g = max(g, int(count))
    res += r * g * b
print(res)
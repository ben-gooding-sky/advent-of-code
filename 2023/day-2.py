f = open("cache/day-2-data", "r")
testData = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

data = f.readlines()
# data = testData

maxRed = 12
maxGreen = 13
maxBlue = 14


def part1():
    total = 0
    for i, game in enumerate(data):
        valid = True
        rounds = [i.split(",") for i in game.split(":")[1].split(";")]
        for pick in rounds:
            for dice in pick:
                [amount, colour] = dice.strip().split(" ")
                if colour == "red":
                    if int(amount) > maxRed:
                        valid = False
                if colour == "green":
                    if int(amount) > maxGreen:
                        valid = False
                if colour == "blue":
                    if int(amount) > maxBlue:
                        valid = False
        if valid:
            total += i + 1

    print(total)

def part2():
    total = 0
    for i, game in enumerate(data):
        maxGreen = 0
        maxRed = 0
        maxBlue = 0
        rounds = [i.split(",") for i in game.split(":")[1].split(";")]
        for pick in rounds:
            for dice in pick:
                [amount, colour] = dice.strip().split(" ")
                if colour == "red":
                    if int(amount) > maxRed:
                        maxRed = int(amount)
                if colour == "green":
                    if int(amount) > maxGreen:
                        maxGreen = int(amount)
                if colour == "blue":
                    if int(amount) > maxBlue:
                        maxBlue = int(amount)
        total += maxGreen * maxBlue * maxRed
    print(total)

# part1()
part2()
# 56314

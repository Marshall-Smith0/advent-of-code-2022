# A = rock
# B = paper
# C = scissors
# 
# X = rock
# Y = paper
# Z = scissors 
#
# 1 for rock
# 2 for paper
# 3 for scissors

# file = open('guide.txt', 'r')
file = [l.strip() for l in open('guide.txt')]
# print(file)

winCount = 0
throwCount = 0

round2Count = 0
round2Throw = 0

for x in file:
    # ROCK
    if x == 'A X':
        winCount = winCount + 3
        throwCount = throwCount + 1
        # need to lose (scissors)
        round2Count = round2Count + 0
        round2Throw = round2Throw + 3
    if x == 'A Y':
        winCount = winCount + 6
        throwCount = throwCount + 2
        # need to draw (rock)
        round2Count = round2Count + 3
        round2Throw = round2Throw + 1
    if x == 'A Z':
        throwCount = throwCount + 3
        # need to win (paper)
        round2Count = round2Count + 6
        round2Throw = round2Throw + 2
    # PAPER
    if x == 'B X':
        throwCount = throwCount + 1
        # need to lose (rock)
        round2Count = round2Count + 0
        round2Throw = round2Throw + 1
    if x == 'B Y':
        winCount = winCount + 3
        throwCount = throwCount + 2
        # need to draw (paper)
        round2Count = round2Count + 3
        round2Throw = round2Throw + 2
    if x == 'B Z':
        winCount = winCount + 6
        throwCount = throwCount + 3
        # need to win (scissors)
        round2Count = round2Count + 6
        round2Throw = round2Throw + 3
    # SCISSORS
    if x == 'C X':
        winCount = winCount + 6
        throwCount = throwCount + 1
        # need to lose (paper)
        round2Count = round2Count + 0
        round2Throw = round2Throw + 2
    if x == 'C Y':
        throwCount = throwCount + 2
        # need to draw (scissors)
        round2Count = round2Count + 3
        round2Throw = round2Throw + 3
    if x == 'C Z':
        winCount = winCount + 3
        throwCount = throwCount + 3
        # need to win (rock)
        round2Count = round2Count + 6
        round2Throw = round2Throw + 1

print(winCount)
print(throwCount)
totalCount = winCount + throwCount
print(totalCount)

print(round2Count)
print(round2Throw)
round2TotalCount = round2Count + round2Throw
print(round2TotalCount)
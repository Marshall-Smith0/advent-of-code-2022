# file = open("elfInput.txt", 'r')
file = [l.strip() for l in open('elfInput.txt')]

calories = []

for elf in ('\n'.join(file)).split('\n\n'):
    # print('elf')
    # print(elf)
    q = 0
    for x in elf.split('\n'):
        q += int(x)
        # print('q')
        # print(q)
    calories.append(q)

# print(max(calories))

calories.sort()

lastThree = calories[-3:]
print(lastThree)

total = sum(lastThree)
print(total)
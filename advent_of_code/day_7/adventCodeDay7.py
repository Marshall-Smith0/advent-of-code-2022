import sys
from collections import defaultdict
inFile = sys.argv[1] if len(sys.argv)>1 else 'directory.txt'
data = open(inFile).read().strip()
lines = [x.strip() for x in data.split('\n')]

# at most 10000
path = []
total_size_directory = defaultdict(int)

for line in lines:
    command = line.strip().split()
    # keeping track of the directory were in
    if command[1] == 'cd':
        # you change directories remove from stack
        if command[2] == '..':
            path.pop()
        else:
            # adding the command to the stack
            path.append(command[2])
    # dont need to do anything when you list the directories
    elif command[1] == 'ls':
        continue
    # same if it is just showing that there is a directory
    elif command[0] == 'dir':
        continue
    else: 
        # you will have a file
        file_size = int(command[0])
        for x in range(1, len(path) + 1 ):
            total_size_directory['/'.join(path[:x])] += file_size

disk_size = total_size_directory['/']
space_needed = disk_size - 40000000

sum1 = 0
sum2 = 1000000000

for i,j in total_size_directory.items():
    # print(i,j)
    if j <= 100000:
        sum1 += j
    if j >= space_needed:
        sum2 = min(sum2, j)

print(sum1)
print(sum2)
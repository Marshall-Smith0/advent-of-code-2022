grid = [list(map(int, line)) for line in open('treePlot.txt').read().splitlines()]

tree1 = 0
tree2 = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        k = grid[r][c]
        # All trees to the left OR right OR above OR below
        if (all(grid[r][x] < k for x in range(c)) or 
        all(grid[r][x] < k for x in range(c + 1, len(grid[r]))) or 
        all(grid[x][c] < k for x in range(r)) or 
        all (grid[x][c] < k for x in range(r + 1, len(grid)))):
            tree1 += 1

        L = R = U = D = 0
        for x in range(c - 1, -1, -1):
            L += 1
            if grid[r][x] >= k:
                break
        for x in range(c + 1, len(grid[r])):
            R += 1
            if grid[r][x] >= k:
                break
        for x in range(r - 1, -1, -1):
            U += 1
            if grid[x][c] >= k:
                break
        for x in range(r + 1, len(grid)):
            D += 1
            if grid[x][c] >= k:
                break
        tree2 = max(tree2, L * R * U * D)        

print(tree1)
print(tree2)

# import sys
# from collections import defaultdict
# inFile = sys.argv[1] if len(sys.argv)>1 else 'treePlot.txt'
# data = open(inFile).read().strip()
# lines = [x.strip() for x in data.split('\n')]

# dir_ = [(-1,0), (0,1), (1,0), (0, -1)]
# grid = []
# for line in lines:
#     grid.append(line)

# rows = len(grid)
# columns = len(grid[0])

# ans1 = 0
# ans2 = 0
# for row in range(rows):
#     for column in range(columns):
#         visible = False
#         for (dr,dc) in dir_:
#             # print(row)
#             # print(column)
#             r = row
#             c = column
#             ok = True
#             while True:
#                 r += dr
#                 c += dc
#                 if not (0<=r<rows and 0<=c<columns):
#                     break
#                 if grid[r][c] >= grid[row][column]:
#                     ok = False
#             if ok:
#                 visible = True
#         if visible:
#             ans1 += 1
# for x in range(rows):
#     for y in range(columns):
#         score = 1
#         for (dr,dc)
# print(ans1)
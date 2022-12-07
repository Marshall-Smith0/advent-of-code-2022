import sys
inFile = sys.argv[1] if len(sys.argv)>1 else 'procedure.txt'
data = open(inFile).read().strip()
lines = [x.strip() for x in data.split('\n')]

S = [
    [], 
    ['R', 'Q', 'G', 'P', 'C', 'F'],
    ['P', 'C', 'T', 'W'],
    ['C', 'M', 'P', 'H', 'B'],
    ['R', 'P', 'M', 'S', 'Q', 'T', 'L'],
    ['N', 'G', 'V', 'Z', 'J', 'H', 'P'],
    ['J', 'P', 'D'],
    ['R', 'T', 'J', 'F', 'Z', 'P', 'G', 'L'],
    ['J', 'T', 'P', 'F', 'C', 'H', 'L', 'N'],
    ['W', 'C', 'T', 'H', 'Q', 'Z', 'V', 'G'],
]
#                         [R] [J] [W]
#             [R] [N]     [T] [T] [C]
# [R]         [P] [G]     [J] [P] [T]
# [Q]     [C] [M] [V]     [F] [F] [H]
# [G] [P] [M] [S] [Z]     [Z] [C] [Q]
# [P] [C] [P] [Q] [J] [J] [P] [H] [Z]
# [C] [T] [H] [T] [H] [P] [G] [L] [V]
# [F] [W] [B] [L] [P] [D] [L] [N] [G]
#  1   2   3   4   5   6   7   8   9 
for cmd in lines: 
    words = cmd.split()
    print(words)
    qty = int(words[1])
    from_ = int(words[3])
    to_ = int(words[5])
    MOVE = S[from_][:qty]
    S[from_] = S[from_][qty:]
    S[to_] = MOVE + S[to_]
    print(qty, from_, to_, S, MOVE)
print(''.join([s[0] for s in S if len(s)>0]))
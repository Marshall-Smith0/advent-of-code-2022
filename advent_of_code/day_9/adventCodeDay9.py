import sys
inFile = sys.argv[1] if len(sys.argv)>1 else 'movement.txt'
data = open(inFile).read().strip()
lines = [x.strip() for x in data.split('\n')]

visited = set([(0, 0)])

head = [0, 0]
tail = [0, 0]

for line in lines:
    x, y = line.split()
    y = int(y)

    for _ in range(y):
        dx = 1 if x == 'R' else -1 if x == 'L' else 0
        dy = 1 if x == 'U' else -1 if x == 'D' else 0

        head[0] += dx
        head[1] += dy

        _x = head[0] - tail[0]
        _y = head[1] - tail[1]

        if abs(_x) > 1 or abs(_y) > 1:
            if _x == 0:
                tail[1] += _y // 2
            elif _y == 0:
                tail[0] += _x // 2
            else:
                tail[0] += 1 if _x > 0 else -1
                tail[1] += 1 if _y > 0 else -1
        visited.add(tuple(tail))

print(len(visited))

rope = [[0,0] for _ in range(10)]
visited_ = set([(0, 0)])

for line in lines:
    x, y = line.split()
    y = int(y)

    for _ in range(y):
        dx = 1 if x == 'R' else -1 if x == 'L' else 0
        dy = 1 if x == 'U' else -1 if x == 'D' else 0

        rope[0][0] += dx
        rope[0][1] += dy

        for i in range(9):
            head_ = rope[i]
            tail_ = rope[i + 1]
            _x = head_[0] - tail_[0]
            _y = head_[1] - tail_[1]

            if abs(_x) > 1 or abs(_y) > 1:
                if _x == 0:
                    tail_[1] += _y // 2
                elif _y == 0:
                    tail_[0] += _x // 2
                else:
                    tail_[0] += 1 if _x > 0 else -1
                    tail_[1] += 1 if _y > 0 else -1
            visited_.add(tuple(rope[-1]))

print(len(visited_))
import sys
inFile = sys.argv[1] if len(sys.argv)>1 else 'packet.txt'
data = open(inFile).read().strip()
lines = [x.strip() for x in data.split('\n')]

p1 = False
p2 = False
for i in range(len(data)):
    print(i)
    if (not p1) and i-3>=0 and len(set([data[i-j] for j in range(4)]))==4:
        print(set([data[i-j] for j in range(4)]))
        print(i+1)
        p1 = True
    if (not p2) and i-13>=0 and len(set([data[i-j] for j in range(14)]))==14:
        print(i+1)
        p2 = True


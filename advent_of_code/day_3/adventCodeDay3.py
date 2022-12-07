counter = 0

# for line in open('ruckSack.txt'):
#     x = line.strip()
#     print(x)
#     string1 = x[:len(x)//2] 
#     string2 = x[len(x)//2:]
#     for c in string1:
#         if c in string2:
#             print(x, string1, string2, c)
#             if 'a'<=c<='z':
#                 # print(ord(c))
#                 # print(ord(c)-ord('a') + 1)
#                 counter += ord(c)-ord('a') + 1
#             else:
#                 # print(ord(c))
#                 # print(ord(c)-ord('A') + 1 + 26)
#                 counter += ord(c)-ord('A') + 1 + 26
#             break
# print(counter)

X = [line for line in open('ruckSack.txt')]
i = 0
while i < len(X):
    for c in X[i]:
        if c in X[i+1] and c in X[i+2]:
            if 'a'<=c<='z':
                counter += ord(c)-ord('a') + 1
            else:
                counter += ord(c)-ord('A') + 1 + 26
            break
    i += 3
print(counter)
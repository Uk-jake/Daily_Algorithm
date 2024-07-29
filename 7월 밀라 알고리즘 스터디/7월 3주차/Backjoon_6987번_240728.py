import sys
input = sys.stdin.readline

result = []

for i in range(4):
    result.append(list(map(int, input().strip().split())))
    
print(result)
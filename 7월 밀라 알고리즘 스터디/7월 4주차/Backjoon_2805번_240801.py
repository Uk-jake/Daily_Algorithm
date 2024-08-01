import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))

print(f"N : {N}, M : {M}")
print(f"trees : {trees}")
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))

# print(f"N : {N}, M : {M}")
# print(f"trees : {trees}")

start = 1
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    
    get_tree = 0
    
    for i in trees:
        if i > mid:
            get_tree += i - mid
    
    if get_tree >= M:
        start = mid + 1
    else :
        end = mid - 1

print(end)
        
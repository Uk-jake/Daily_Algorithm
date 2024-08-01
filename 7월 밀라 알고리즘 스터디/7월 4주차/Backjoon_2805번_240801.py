import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))

# 시작 위치는 1, 끝 위치는 나무 중 가장 큰 나무
start = 1
end = max(trees)

# 이분 탐색을 통해 끝 위치의 최소 값을 찾는다.
while start <= end:
    mid = (start + end) // 2
    
    get_tree = 0
    # 나무의 길이가 절단기 길이 보다 작으면 음수가 나오기 때문에 if문 사용
    for i in trees:
        if i > mid:
            get_tree += i - mid
    
    # 자른 나무의 길이가 M보다 크면 시작 인덱스를 중간 + 1 값으로 조정
    if get_tree >= M:
        start = mid + 1
    # 자른 나무의 길이가 M보다 작으면 끝 인덱스를 중간 - 1 값으로 조정
    else :
        end = mid - 1

print(end)
        
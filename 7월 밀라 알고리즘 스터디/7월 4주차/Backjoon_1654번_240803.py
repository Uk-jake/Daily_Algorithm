import sys
input = sys.stdin.readline

# 이분 탐색을 통한 랜선의 길이 조정
def get_line():

    start = 1
    end = max(lines)

    while start <= end:
        mid = (start + end)//2

        # 얻을 수 있는 랜선의 길이가 N보다 크거나 같다면 start 값을 조정
        # 얻을 수 있는 랜선의 길이가 N보다 작다면 end 값 조정
        if cut_line(mid):
            start = mid + 1
        else:
            end = mid - 1

    return start - 1

# length 길이로 얻을 수 있는 랜선의 개수 구하는 함수
# 얻을 수 있는 개수가 N보다 크거나 같다면 True
# 얻을 수 있는 개수가 N보다 작다면 False
def cut_line(length):

    result = 0

    for i in lines:
        result += i // length
        
    if result >= N:
        return True
    else:
        return False


# K - 이미 가지고 있는 랜선의 개수
# N - 필요한 랜선의 개수
K, N = map(int, input().strip().split())

# 가지고 있는 랜선 리스트
lines = []

for _ in range(K):
    lines.append(int(input().strip()))

print(get_line())
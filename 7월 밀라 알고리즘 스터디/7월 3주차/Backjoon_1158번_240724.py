import sys
input = sys.stdin.readline

# 백트래킹
# n 인덱스 및 몇번 반복했는지
# sum 선택한 정수들의 합
# 선택한 정수의 개수
def backtracking(n, sum, count):
    
    global answer
    
    # 인덱스를 모두 사용했을 떄
    if n == N:
        # 합계가 S이고 요소를 한개 이상 선택했을 때 
        if sum == S and count > 0:
            answer += 1
        return
        
    # 다음 요소를 선택했을 떄
    backtracking(n + 1, sum + nums[n], count + 1)
    # 다음 요소를 선택안했을 때
    backtracking(n + 1, sum, count)
        
        

N, S = map(int, input().strip().split())

nums = list(map(int, input().strip().split()))

answer = 0

backtracking(0, 0, 0)
print(answer)
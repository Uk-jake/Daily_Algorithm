import sys
input = sys.stdin.readline

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

def solution(n, times):
    # 이분 탐색의 범위 설정
    left = 1
    right = max(times) * n
    
    # 이분 탐색
    while left <= right:
        mid = (left + right) // 2
        
        # 중간 시간 동안 각 심사관이 처리할 수 있는 사람의 수 계산
        total_people = sum(mid // time for time in times)
        
        # 모든 사람이 심사를 받을 수 있는지 확인
        if total_people >= n:
            right = mid - 1
        else:
            left = mid + 1
    
    # 최소 시간 반환
    return left

# 예제 입력
n = 6
times = [7, 10]

# 예제 출력
print(solution(n, times))  # 28
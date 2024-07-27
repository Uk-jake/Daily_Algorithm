def check(seq):
    # 현재까지의 수열에서 나쁜 수열이 되는지 검증하는 함수
    length = len(seq)
    for i in range(1, length // 2 + 1):
        # 부분 수열이 동일한지 확인
        if seq[-i:] == seq[-2*i:-i]:
            return False
    return True

def backtrack(seq, n):
    # 백트래킹을 통해 좋은 수열을 생성하는 함수
    if len(seq) == n:
        # 길이가 n인 좋은 수열을 찾으면 출력하고 종료
        print(seq)
        return True

    for i in '123':
        # 새로운 숫자를 추가하여 나쁜 수열인지 확인
        if check(seq + i):
            # 좋은 수열이면 계속 탐색
            if backtrack(seq + i, n):
                return True

    return False

N = int(input().strip())

# 백트래킹 시작
backtrack('', N)

import sys
input = sys.stdin.readline

# 백트래킹 함수 정의
def backtracking(pre_word, picked):
    # 만약 모든 문자를 선택했다면, 가능한 경우 하나를 찾은 것이므로 1을 반환
    if picked == len(S):
        return 1

    answer = 0  # 가능한 경우의 수를 저장할 변수
    # 모든 문자를 키로 가지는 딕셔너리 counter를 순회
    for key in counter.keys():
        # 이전에 선택한 문자와 현재 선택하려는 문자가 같다면 건너뜀
        if pre_word == key:
            continue
        # 현재 문자의 개수가 0이라면 건너뜀
        if counter[key] == 0:
            continue
        
        # 현재 문자를 선택하고 개수를 감소
        counter[key] -= 1
        # 재귀 호출하여 다음 문자를 선택
        answer += backtracking(key, picked + 1)
        # 재귀 호출이 끝난 후 선택한 문자의 개수를 복구
        counter[key] += 1
    
    return answer

# 입력받은 문자열을 리스트로 변환
S = list(input().strip())

# 각 문자의 개수를 세어 저장할 딕셔너리 초기화
counter = dict()
for s in S:
    if s in counter:
        counter[s] += 1
    else:
        counter[s] = 1

# 백트래킹 함수 호출하여 가능한 모든 경우의 수 계산
answer = backtracking('', 0)

# 결과 출력
print(answer)
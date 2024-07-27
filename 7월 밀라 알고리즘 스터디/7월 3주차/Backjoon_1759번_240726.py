def backtrack(path, index, vowels_count, consonants_count):
    # 경로 길이가 L이면 종료 조건
    if len(path) == L:
        # 최소 한 개의 모음과 두 개 이상의 자음을 포함하는지 확인
        if vowels_count >= 1 and consonants_count >= 2:
            result.append("".join(path))
        return

    for i in range(index, C):
        char = chars[i]
        # 모음인지 자음인지 판별
        if char in vowels:
            backtrack(path + [char], i + 1, vowels_count + 1, consonants_count)
        else:
            backtrack(path + [char], i + 1, vowels_count, consonants_count + 1)


# 입력 처리
L, C = map(int, input().strip().split())
chars = input().strip().split()

# 모음과 자음 구분
vowels = set('aeiou')
chars.sort()

result = []

# 백트래킹 호출
backtrack([], 0, 0, 0)

# 결과 출력
print("\n".join(result))
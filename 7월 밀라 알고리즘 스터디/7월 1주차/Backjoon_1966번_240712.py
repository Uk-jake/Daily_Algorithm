def print_order(input_list, n, m):

    # 문자열 리스트를 정수형 리스트로 변환
    print_queue = [int(value) for value in input_list]
    
    idx = 0
    count = 0

    while True:
        
        # 나머지 연산자를 이용하여 idx를 항상 배열의 크기보다 작거나 같도록 유지
        idx = idx % n        
        
        # 출력할 문서의 값과 리스트의 최대 값 비교
        # 우선 순위가 가장 높다면 출력
        if print_queue[idx] >= max(print_queue):
            # 출력 시 count 1 증가
            count += 1

            # 출력한 문서가 몇번재로 인쇄되었는지 궁금했던 문서이면 break
            if (idx == m):
                break

            # 출력한 문서는 0으로 변경
            print_queue[idx] = 0

        # 다음 문서를 확인하기 위해 idx 1 증가
        idx += 1
    
    return count

# Testcase 개수 입력
testcase_count = int(input().strip())
answer_list = []

for i in range(testcase_count):
    # 테스트 케이스 N(문서 개수), M(몇번째로 인쇄되었는지 궁금한 문서의 순서) 입력
    n, m = map(int, input().strip().split())
    # 문서 중요도 입력
    print_queue = input().strip().split()
    # 문서 중요도에 따라 인쇄 함수
    answer_list.append(print_order(print_queue, n, m))
    
# 각 테스트 케이스들의 결과 값 출력
for i in answer_list:
    print(i)
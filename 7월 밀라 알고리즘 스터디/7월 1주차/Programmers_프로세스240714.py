def solution(priorities, location):
    answer = 0
    idx = 0
    
    while True:
        
        idx = idx % len(priorities)
        
        if priorities[idx] >= max(priorities):
            priorities[idx] = 0
            answer += 1
            if location == idx :
                break
        
        idx += 1

    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))
# print("!")
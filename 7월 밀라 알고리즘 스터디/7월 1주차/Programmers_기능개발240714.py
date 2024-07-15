import math
from collections import deque

def solution(progresses, speeds):
    remain_day = []
    answer = []
    
    for i in range(len(progresses)):
        tmp = (100 - progresses[i]) / speeds[i]
        remain_day.append(math.ceil(tmp))
    
    idx = -1
    stack = deque()
    
    for item in remain_day:    
        if len(stack) == 0 :
            stack.append(item)
            idx += 1
            answer.append(1)
        elif stack[0] >= item:
            answer[idx] += 1
        else :
            idx += 1
            answer.append(1)

    return answer


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

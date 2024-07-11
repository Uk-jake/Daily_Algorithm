from collections import deque

def check_vps(data):
    
    stack = deque()
    
    print(f"data : {data}")
    
    for i in data:
        print(f"i : {i}")
        
        if len(stack) == 0 and i == ')':
            return "NO"
        elif i == '(':
            stack.append(i)
        elif i == ')':
            stack.pop()
    
    print(f"len(stack) : {len(stack)}")
    print(f"stack : {stack}")
    
    if len(stack) == 0:
        return "YES"
    else :
        return "NO"
        

num_input = int(input().strip())

answer_list = []

for i in range(num_input):
    ps_input = input().strip()
    answer_list.append(check_vps(ps_input))
    
for i in answer_list:
    print(i)
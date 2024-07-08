# 연결 리스트로 Stack 자료구조 구현
class Node:
    def __init__(self, data):
        # 노드 데이터 초기화
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        # 스택 최상위 노드와 스택의 길이 초기화
        self.topNode = None
        self.len = 0

    def push(self, data):
        # 새로운 데이터 스택에 추가
        if self.topNode is None:
            # 스택이 비어 있으면 새 노드를 topNode로 설정
            node = Node(data)
            self.topNode = node
            self.len += 1
        else:
            # 스택이 비어 있지 않으면 새 노드를 생성하고
            # 현재 topNode를 새로운 노드의 다음 노드로 설정한 후 
            # 새로운 노드를 topNode로 설정
            node = Node(data)
            node.next = self.topNode
            self.topNode = node
            self.len += 1

    def pop(self):
        # 스택의 topNode를 제거하고 그 데이터를 반환
        if self.topNode is None:
            # 스택이 비어있으면 -1 반환
            return -1
        else:
            # 현재 topNode 를 저장하고 topNode를 다음 노드로 변경
            node = self.topNode
            self.topNode = self.topNode.next
            self.len -= 1
            # 제거된 노드의 데이터 반환
            return node.data

    def size(self):
        # 스택의 크기를 반환
        return self.len

    def empty(self):
        # 스택이 비어 있는지 확인
        if (self.len == 0) and (self.topNode is None):
            return 1
        else:
            return 0

    def top(self):
        # 스택의 topNode의 데이터 반환
        if self.topNode is None:
            # 스택이 비어있으면 -1 반환
            return -1
        else:
            # topNode 데이터를 반환
            return self.topNode.data
    
# 스택 객체 생성
stack = Stack()
# 출력 결과를 저장할 배열
printArray = []

# 명령어의 개수 입력
orderCount = int(input())

# 명령어 개수만큼 반복
for i in range(orderCount):
    # 명령어 입력
    order = input().strip()
    
    # 명령어에 따라 스택 연산 수행
    if order.startswith('push'):
        # push 명령어 처리
        orderText, orderNum = order.split()
        stack.push(orderNum)
    elif order == 'pop':
        # pop 명령어 처리
        printArray.append(stack.pop())
    elif order == 'size':
        # size 명령어 처리
        printArray.append(stack.size())
    elif order == 'empty':
        # empty 명령어 처리
        printArray.append(stack.empty())
    elif order == 'top':
        # top 명령어 처리
        printArray.append(stack.top())
        
# 모든 연산 결과 출력
for i in printArray:
    print(i)
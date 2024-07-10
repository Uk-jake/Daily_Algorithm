import queue

def solution(bridge_length, weight, truck_weights):
    bridge_queue = queue.Queue()
    answer_list = []
    answer = 0
    idx = 0
    bridge_weight = 0    
    
    # 다리 길이 만큼 큐의 초기 값을 0으로 선언
    for i in range(bridge_length):
        bridge_queue.put(0)
    
    # answer_list에 모든 트럭이 도착하였다면 while문 정지
    # while문이 한번 씩 반복 될 때 마다 1초가 지날 때 발생하는 일들을 작성함
    while len(answer_list) != len(truck_weights):
        
        # 1초 증가
        answer += 1
        
        # 도착한 트럭은 bridge_queue에서 삭제, bridge_weight(현재 다리에 올라가있는 트럭들의 무게)에서 차감
        arrvied_truck = bridge_queue.get()
        bridge_weight -= arrvied_truck
        
        # 도착한 트럭이 0이면 아무것도 도착하지 않은 것
        # 0이 아니면 arrived_list에 추가
        if arrvied_truck != 0:
            answer_list.append(arrvied_truck)
        
        bridge_weight += truck_weights[idx]
        
        # 다음 순서의 트럭이 올라갔을 때 무게가 초가된다면 queue에 0 값 추가
        if bridge_weight > weight:
            bridge_queue.put(0)
            bridge_weight -= truck_weights[idx]
        # 초과되지 않는다면 queue에 트럭 추가
        elif bridge_weight <= weight:
            bridge_queue.put(truck_weights[idx])
            idx += 1
            if idx >= len(truck_weights):
                idx -= 1
    
    return answer


print( solution(2, 10, [7, 4, 5, 6]) )
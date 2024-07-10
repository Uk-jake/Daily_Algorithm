import queue


def solution(bridge_length, weight, truck_weights):
    bridge_queue = queue.Queue()
    answer = 0
    bridge_weight = 0

    # 다리 길이 만큼 큐의 초기 값을 0으로 선언
    for i in range(bridge_length):
        bridge_queue.put(0)

    while len(truck_weights) > 0 :

        # 1초 증가
        answer += 1

        # 도착한 트럭은 bridge_queue에서 삭제, bridge_weight(현재 다리에 올라가있는 트럭들의 무게)에서 차감
        bridge_weight -= bridge_queue.get()

        if bridge_weight + truck_weights[0] <= weight:
            bridge_weight += truck_weights[0]
            print(f"truck_weight[0] : {truck_weights[0]}")
            bridge_queue.put(truck_weights.pop(0))
        else :
            bridge_queue.put(0)
            
        # print(f"bridge_queue : {bridge_queue}")
        print(f"answer : {answer}")

    answer += bridge_length
    
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge_t = deque([])
    cnt = 0 # 다리 무게 저장하는 변수
    answer = 0
    while True:
        # 두개의 리스트 모두 빈 리스트이면 반복문 종료
        if not bridge_t and not truck_weights:
            break
        if truck_weights:
            # 대기 트럭 맨 앞이 다리를 건널 수 있으면
            if (cnt + truck_weights[0]) <= weight:
                # print(truck_weights[0])
                cur = truck_weights.popleft()
                cnt += cur # 다리에 무게 더해주기
                bridge_t.append([cur, 0]) # 현재 트럭과 다리 위치도 함께 저장
            
        # 한 트럭씩 앞으로 이동 시켜주는 코드
        for b in bridge_t:
            b[1] += 1
        # 다리를 넘어가버리면 빼주기
        if bridge_t[0][1] == bridge_length:
            cnt -= bridge_t[0][0]
            bridge_t.popleft()
        answer += 1
                   
    
    
    
    return answer
print(solution(2, 10, [7,4,5,6]))
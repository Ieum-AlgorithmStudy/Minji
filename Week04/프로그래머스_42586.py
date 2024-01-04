def solution(progresses, speeds):
    answer = []
    result = [] # 차이값 리스트
    # 각각의 작업 진도와 속도 값을 고려해서 며칠이 걸리는지 리스트에 담아주는 코드
    for i in range(len(progresses)):
        cnt = 0 # 며칠 걸리는지 변수
        cur = progresses[i] # 비교할 위치 담을 변수
        # 100보다 같거나 커질때까지 계속 반복
        while cur < 100:
            cnt += 1
            cur += speeds[i]
        # 반복문 종료되면 리스트에 담아주기(며칠값)
        result.append(cnt)
    # 배포가 앞에 보다 뒤에가 더 일찍 끝나면 한번에 끝남
    # -> cnt를 높여줌
    # 배포가 뒤에 값이 더 크게 되면 위치 초기화 시켜주고 리스트에 1넣어줌
    check = result[0] # 체크할 위치
    a = 1 # 한번에 배포 되는 양을 담은 변수
    # 첫 값을 먼저 변수에 넣어주고 뒤에부터 비교 시작
    for r in result[1:]:
        if check >= r:
            a += 1
        else:
            check = r
            answer.append(a)
            a = 1
    # 마지막 값은 안들어가기에, for문이 종료되면 값을 넣어줌
    answer.append(a)            
    return answer

# 보완
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
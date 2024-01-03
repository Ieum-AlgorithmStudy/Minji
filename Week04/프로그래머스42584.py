def solution(prices):
    N = len(prices)
    answer = []
    for i in range(N-2):
        print(i,"시작")
        cnt = 0
        for j in range(i+1, N):
            print(j)
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
    
        answer.append(cnt)
    answer.append(1)
    answer.append(0)
    return answer
print(solution([1,2,3,4,5,2,3]))
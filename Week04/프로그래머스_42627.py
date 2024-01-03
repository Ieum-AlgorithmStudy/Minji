def solution(jobs):
    N = len(jobs)
    stack = []
    visited = [0] * N
    answer = []
    def backTracking():
        # 작업 시간 구하는 코드
        if len(stack) == N:
            cnt = 0
            result = 0
            for s in stack:
                cnt += s[1]
                result += (cnt - s[0])
            answer.append((result//N))
            return
        for i in range(N):
            if visited[i] == 0:
                stack.append(jobs[i])
                visited[i] = 1
                backTracking()
                stack.pop()
                visited[i] = 0
        return
    backTracking()    
    
    
    return min(answer)
print(solution([[0, 3], [1, 9], [2, 6]]))
# -> 백트레킹으로 모든 경우의 수를 다 구하는 것은 자료의 양이 너무 많아지면 효율성에서 실패가 뜸
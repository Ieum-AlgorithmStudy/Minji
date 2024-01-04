from collections import Counter
def solution(clothes):
    answer = 1
    # 의상의 종류를 세어 딕셔너리 형태로 만들어준다.
    stack = []
    for _, i in clothes:
        stack.append(i)
    clothes_Counter = Counter(stack)
    
    # 종류에 +1을 해줘 answer에 곱해준다.
    for j in clothes_Counter.values():
        answer *= j+1
    answer -= 1
    return answer
def solution(genres, plays):
    answer = []
    result_dic = {}

    # 합산 딕셔너리 만들기
    for i in range(len(plays)):
        if genres[i] in result_dic:
            result_dic[genres[i]] += plays[i]
        else:
            result_dic[genres[i]] = plays[i]
    # 베스트 앨범 뭔지 알아보기
    result_dic = sorted(result_dic.items(), key=lambda x : x[1], reverse=True)
    
    # 장르에 따라 (노래횟수,인덱스) 값 넣어주기
    temp = zip(genres, plays, range(len(plays)))
    temp = sorted(temp, key=lambda x : (x[0], -x[1], x[2]))
    
   # 베스트 앨범끼리 먼저 2개 담아주기
    for d in result_dic:
        cnt = 0
        for t in temp:
            if d[0] == t[0]:
                cnt += 1
                if cnt > 2:
                    break
                else:
                    answer.append(t[2])
                               
    
    return answer
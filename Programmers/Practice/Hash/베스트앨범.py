def solution(genres, plays):
    answer = []
    g_dict = dict()
    p_dict = dict()
    for i in range(len(genres)):
        if genres[i] in g_dict:
            g_dict[genres[i]] += plays[i]
            p_dict[genres[i]].append((plays[i], i))
        else:
            g_dict[genres[i]] = plays[i]
            p_dict[genres[i]] = [(plays[i],i)]
    g_dict = sorted(g_dict.items(), key = lambda item: item[1], reverse = True)
    for g in g_dict:
        genre = g[0]
        p_dict[genre].sort(key=lambda item:(-item[0],item[1]))
        cnt = 0
        for i in range(len(p_dict[genre])):
            cnt +=1
            answer.append(p_dict[genre][i][1])
            if cnt == 2:
                break
    return answer

genres = ["classic", "pop", "classic", "classic", "pop", "pop"]
plays = [500, 600, 150, 800, 2500, 2500]
print(solution(genres, plays))
# 코딩테스트 연습 : Hash Level2
# 중간에 tuple 정렬할때 첫 원소와 두번째 원소의 정렬 방식 다르게 하는 법 알아두자!!

def solution(money):
    #첫번째 집 털기-> 마지막 집도 못 턴다
    f_h=[money[0],money[0]+0]
    for i in range(2,len(money)-1):
        f_h.append(max(f_h[i-2]+money[i],f_h[i-1]))
    #첫번쨰 집 안털기-> 마지막 집 털수 있다
    s_h=[0,money[1]]
    for i in range(2,len(money)):
        s_h.append(max(s_h[i-2]+money[i],s_h[i-1]))
    return max(f_h[-1],s_h[-1])
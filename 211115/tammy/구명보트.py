def solution(people, limit):
    people.sort(reverse=True) # 몸무게 역순으로 sort

    cnt = 0
    idx = len(people) - 1  # 리스트 끝을 가리킬 인덱스변수

    for i in range(len(people)):
        if i > idx : # 태운사람은 더이상 태우면 안되므로 인덱스가 교차될 시, for문 끝내기
            break
        if people[i] == limit or people[i]+people[idx] > limit : # people[i]만 태우는 상황
            cnt += 1
            continue

        elif people[i]+people[idx] <= limit: # 두사람을 태우는 경우
            idx -= 1 # people[idx]태웠으므로, idx -1해주기
            cnt +=1 # cnt +1

    return cnt


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))

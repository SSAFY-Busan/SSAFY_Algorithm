from collections import deque
def solution(people, limit):
    people.sort()
    people=deque(people)
    cnt=0
    while len(people)>1:
        if people[0]+people[-1]<=limit:
            people.popleft()
            people.pop()
        else:
            people.pop()
        cnt+=1
    if people:
        cnt+=1
    return cnt
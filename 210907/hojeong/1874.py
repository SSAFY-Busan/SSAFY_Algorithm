# 스택 수열
n = int(input())  # 1~n까지 숫자가 n개 들어온다.
goal = [int(input()) for _ in range(n)]  # 원하는 수열
stack = []  # 스택
method = []  # 출력 리스트
s = 0  # 수열 인덱스
num = 1  # 숫자 1~n까지니깐 1로 초기화
ans = True  # 수열이 만들어 지는지 확인
while num <= n:  # n까지 스택에 들어갔다면 더이상 append 할 필요는 없고 남은 스택을 pop할 일만 남는다.
    if num <= goal[s]:  # 숫자와 수열을 비교  ex) 1< goal[0](4)
        stack.append(num)  # 스택에 1 추가
        method.append('+')  # 메서드엔 +추가
        if num == goal[s]:  # 숫자가 4 까지 추가된 상태에서 4=goal[0]
            stack.pop()  # 해당 숫자를 팝
            method.append('-')  # 메서드 -추가
            s += 1  # 다음 수열 인덱스로
        num += 1  # 만약 숫자와 수열과 다르면 숫자를 1증가

    else:  # 숫자가 수열값보다 작은 경우는 이미 그 수가 append되어있다는 뜻 (오름차순으로 추가되기때문)
        k = stack.pop()
        method.append('-')
        if k != goal[s]:  # top과 수열이 같아야함 -> 다르면 하나 더 뽑게 되는데 그러는 순간 수열을 못만듬
            ans = False
            break
        s += 1
for i in range(len(stack)):  # 이젠 남은 stack을 차레대로 빼주면서 그값과 수열을 비교
    if goal[s] == stack.pop():
        method.append('-')
        s += 1
    else:
        ans = False
        break
if ans:
    for i in method:
        print(i)
else:
    print('NO')

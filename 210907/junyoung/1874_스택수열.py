# 스택 수열

# 스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다.
# 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는
# (LIFO, Last in First out) 특성을 가지고 있다.
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때
# 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
# 이를 계산하는 프로그램을 작성하라.

#첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는
# 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

n = int(input())                 # 입력받고
ans = []                         # 정답 리스트
stack = []                       # 스택 리스트
cnt = 0                          # 카운트
for i in range(n):               # n 번 반복
    num = int(input())           # 숫자 입력
    while True:                  # 반복
        if cnt < num:            # cnt 가 입력수 보다 작으면
            cnt += 1             # 1씩 증가하고
            stack.append(cnt)    # 스택에 cnt 추가
            ans.append('+')      # 정답에 + 추가
        else:                    # cnt 가 num 이랑 같거나 크면
            break                # 멈춰

    if stack[-1] == num:         # 다돌고 스택의 마지막 값이 num 과 같으면
        stack.pop()              # 팝하고
        ans.append('-')          # -를 정답에 추가
    else:                        # 같지않으면 불가능한 경우이므로 
        ans = 'NO'               # ans 를 NO 로 초기화
        break                    # 스톱
if ans == 'NO':                  # 만약 NO 이면
    print(ans)                   # NO 출력
else:                            # 정상적이라면
    for i in ans:                # 반복해서 하나씩 출력
        print(i)

    
# 스위치 켜고 끄기

# 1부터 연속적으로 번호가 붙어있는 스위치들이 있다. 스위치는 켜져 있거나 꺼져있는 상태이다.
# <그림 1>에 스위치 8개의 상태가 표시되어 있다. ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다.
# 그리고 학생 몇 명을 뽑아서, 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어주었다.
# 학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작하게 된다.
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
# 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다. <그림 1>과 같은 상태에서 남학생이 3을 받았다면,
# 이 학생은 <그림 2>와 같이 3번, 6번 스위치의 상태를 바꾼다.
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서,
# 그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

# 첫째 줄에는 스위치 개수가 주어진다. 스위치 개수는 100 이하인 양의 정수이다. 둘째 줄에는 각 스위치의 상태가 주어진다.
# 켜져 있으면 1, 꺼져있으면 0이라고 표시하고 사이에 빈칸이 하나씩 있다. 셋째 줄에는 학생수가 주어진다.
# 학생수는 100 이하인 양의 정수이다. 넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어진다.
# 남학생은 1로, 여학생은 2로 표시하고, 학생이 받은 수는 스위치 개수 이하인 양의 정수이다.
# 학생의 성별과 받은 수 사이에 빈칸이 하나씩 있다.
        
N = int(input())                                        # 입력
switch = [-1] + list(map(int, input().split()))         # 스위치의 인덱스를 맞추기 위해서 맨앞에 0 인덱스에 -1 을 넣는다
students = int(input())                                 # 학생 수 
for s in range(students):                               # 학생수 만큼 반복
    gene, num = map(int, input().split())               # 성별과 스위치 번호 

    if gene == 1:                                       # 남학생이면
        for i in range(num, N+1, num):                  # 번호의 배수만큼 점프
            if switch[i] == 0:                          # 꺼져있으면
                switch[i] = 1                           # 키고
            else:                                       # 켜져있으면
                switch[i] = 0                           # 끈다

    if gene == 2:                                       # 여학생이면
        if switch[num] == 0:                            # 꺼져있으면
            switch[num] = 1                             # 키고
        else:                                           # 켜져있으면
            switch[num] = 0                             # 끈다
        jump = 0                                        # 점프할 변수
        for i in range(N//2):                           # 스위치의 반만큼 반복
            if num - i > 0 and num + i <= N:            # 인덱스 범위 조절
                if switch[num - i] == switch[num+i]:    # 자신의 양쪽 같이 같다면
                    jump += 1                           # 점프수 1 증가
                else:                                   # 다르면
                    break                               # 스톱
        for j in range(1, jump):                        # 점프할 번수만큼 반복
            if switch[num - j] == 0:                    # 어차피 양쪽이 같으니깐 한쪽만 비교 : 꺼져있으면
                switch[num - j], switch[num + j] = 1, 1 # 양쪽을 킨다
            elif switch[num - j] == 1:                  # 켜져있으면
                switch[num - j], switch[num + j] = 0, 0 # 양쪽을 끈다

for i in range(1, N+1):                                 # N + 1 반복
    print(switch[i], end=' ')                           # 스위치 상태 표시
    if i % 20 == 0:                                     # 20개 넘어가면 줄 바꾸기
        print()
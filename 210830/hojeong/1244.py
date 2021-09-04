# 스위치 켜고 끄기
def check_switch1(key):  # 남자일 경우
    nums = []
    for i in range(1, N + 1):
        if i % key == 0:
            nums.append(i - 1)  # 인덱스로 저장

    return nums


def check_switch2(key):
    nums = [key]  # 자기자신 포함
    for i in range(1, (N + 1) // 2):
        if 0 <= key - i and key + i < N:  # 범위 조건
            if switch[key - i] == switch[key + i]:
                nums.append(key - i)
                nums.append(key + i)
            else:
                return nums  # 다른 순간 탈출

    return nums


N = int(input())  # 스위치 개수
switch = list(map(int, input().split()))  # 스위치 상태 1:ON 0:OFF

P = int(input())  # 학생수
for i in range(P):  # 1:남자 2: 여자
    s, n = map(int, input().split())
    if s == 1:
        change = check_switch1(n)  # 배수 조건이 있으므로 그대로
    else:
        change = check_switch2(n - 1)  # 인덱스로 계산해야하기 때문에

    for i in change:
        if switch[i] == 1:
            switch[i] = 0
        else:
            switch[i] = 1
# 출력하기

if N > 20:
    for i in range(N // 20):
        print(*switch[:20])
        switch = switch[20:]

print(*switch)

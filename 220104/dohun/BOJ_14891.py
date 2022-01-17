from collections import deque

wheel1 = deque(map(int, input()))
wheel2 = deque(map(int, input()))
wheel3 = deque(map(int, input()))
wheel4 = deque(map(int, input()))

# K는 회전횟수
K = int(input())
for _ in range(K):
    # number = 톱니바퀴번호, direction = 방향
    number, direction = map(int, input().split())
    array = deque([direction])

    # 1번 톱니바퀴
    if number == 1:
        # 접점이 다르면 방향 반대 추가
        if wheel1[2] != wheel2[6]:
            array.append(-direction)
            # 접점이 다르면 방향 반대 추가
            if wheel2[2] != wheel3[6]:
                array.append(direction)
                # 접점이 다르면 방향 반대 추가
                if wheel3[2] != wheel4[6]:
                    array.append(-direction)
                # 접점이 같으면 움직이지 않게 0추가
                else:
                    array.append(0)
            # 접점이 같으면 움직이지 않게 0추가
            else:
                array.append(0)
                array.append(0)
        # 접점이 같으면 움직이지 않게 0추가
        else:
            array.append(0)
            array.append(0)
            array.append(0)

    # 2번 톱니바퀴
    elif number == 2:
        if wheel1[2] != wheel2[6]:
            array.appendleft(-direction)
        else:
            array.appendleft(0)
        if wheel2[2] != wheel3[6]:
            array.append(-direction)
            if wheel3[2] != wheel4[6]:
                array.append(direction)
            else:
                array.append(0)
        else:
            array.append(0)
            array.append(0)

    # 3번 톱니바퀴
    elif number == 3:
        if wheel2[2] != wheel3[6]:
            array.appendleft(-direction)
            if wheel1[2] != wheel2[6]:
                array.appendleft(direction)
            else:
                array.appendleft(0)
        else:
            array.appendleft(0)
            array.appendleft(0)
        if wheel3[2] != wheel4[6]:
            array.append(-direction)
        else:
            array.append(0)

    # 4번 톱니바퀴
    elif number == 4:
        if wheel3[2] != wheel4[6]:
            array.appendleft(-direction)
            if wheel2[2] != wheel3[6]:
                array.appendleft(direction)
                if wheel1[2] != wheel2[6]:
                    array.appendleft(-direction)
                else:
                    array.appendleft(0)
            else:
                array.appendleft(0)
                array.appendleft(0)
        else:
            array.appendleft(0)
            array.appendleft(0)
            array.appendleft(0)

    # 회전시키기 1일경우 시계방향(오른쪽) -1일 경우 반시계(왼쪽으로)
    wheel1.rotate(array[0])
    wheel2.rotate(array[1])
    wheel3.rotate(array[2])
    wheel4.rotate(array[3])

# 확인해서 점수 더하기
cnt = 0
if wheel1[0] == 1:
    cnt += 1
if wheel2[0] == 1:
    cnt += 2
if wheel3[0] == 1:
    cnt += 4
if wheel4[0] == 1:
    cnt += 8

print(cnt)
N = int(input()) # 스위치 개수
arr = list(map(int, input().split())) # 스위치 상태
student = int(input()) # 학생 수
for _ in range(student):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(len(arr)):
            if (i + 1) % number == 0:
                if arr[i] == 0:
                    arr[i] = 1
                elif arr[i] == 1:
                    arr[i] = 0

    elif gender == 2:
        if arr[number-1] == 1:
            arr[number-1] = 0
        elif arr[number] == 0:
            arr[number-1] = 1
        idx = 1
        while (number-1 - idx >= 0 and number-1 + idx < N and arr[number-1-idx] == arr[number-1+idx]):
            if arr[number-1+idx] == 1:
                arr[number-1+idx] = 0
                arr[number-1-idx] = 0
            elif arr[number-1+idx] == 0:
                arr[number-1+idx] = 1
                arr[number-1-idx] = 1
            idx += 1

for i in range(len(arr)):
    if i % 20 == 0:
        print()
    print(arr[i], end=" ")
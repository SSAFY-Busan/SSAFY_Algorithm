# 접미사 배열
s = input()  # 문자 입력
lst = [s]  # 리스트에 원본을 넣고 초기화
n = len(s) - 1  # 문자열 개수는 글자수, 원본은 빼줌
while n:  # n이 0이 되면 탈출
    s = s[1:]  # 슬라이싱
    lst.append(s)  # 추가
    n -= 1  # 횟수 1감소
lst.sort()
for i in lst:
    print(i)

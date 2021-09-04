# replace 사용하여 길이 비교 가능
cro_lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
alphabet = input()

idx = 0 # 인덱스 번호
cnt = 0 # 횟수
while True:
    # cro_lst에 들은 문자열 3개짜리일 경우 인덱스 +3
    if alphabet[idx:idx+3] in cro_lst:
        idx += 3
    # cro_lst에 들은 문자열 2개짜리일 경우 인덱스 +2
    elif alphabet[idx:idx+2] in cro_lst:
        idx += 2
    # 나머지는 인덱스 += 1
    else:
        idx += 1
    # 갯수 +1 추가
    cnt += 1

    # 인덱스가 원래 길이보다 넘어설 경우 종료
    if idx >= len(alphabet):
        break

print(cnt)

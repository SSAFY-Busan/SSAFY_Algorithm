# 방 번호
N = list(map(int, input()))  # 숫자 하나씩 리스트로
counting = [0] * 10  # 0부터 9까지 갯수를 담을 리스트
for i in N:  # 리스트를 순회
    if i == 6 or i == 9:  # 만약 6이나 9일 경우에는 각 숫자의 카운팅의 수가 적은거에 +1 해준다
        if counting[6] == counting[9]:  # 예를 들면 6은 2개 9는 0개일 경우
            counting[i] += 1  # 처음 6은 6과 9의 카운팅 수가 같으니 카운팅 6에 1증가하지만 ->counting[6]=1, counting[9]=0
        elif counting[6] > counting[9]:  # 두번째 6이 들어왔을 때는 카운팅 수가 작은 9번 인덱스에 +=1 증가한다.
            counting[9] += 1  # counting[6]=1,counting[9]+=1 --> 6과 9를 뒤집어 사용하는 경우가 고려된다.
        else:
            counting[6] += 1
    else:
        counting[i] += 1
print(max(counting))

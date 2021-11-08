array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1], [1,7,3]]

def solution(array, commands):
    answer = []
    # 차례대로 순서 찾기
    for i in range(len(commands)):
        # 시작, 끝, 위치 지점
        start = commands[i][0] - 1
        end = commands[i][1]
        idx = commands[i][2] - 1

        # 새로운 리스트 가져오기
        copy_lst = array[start:end]
        # 정렬하기
        copy_lst.sort()
        # 해당 위치 정답에 넣기
        answer.append(copy_lst[idx])
    return answer

print(solution(array, commands))
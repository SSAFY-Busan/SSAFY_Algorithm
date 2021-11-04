def solution(array, commands):
    answer = []
    for c in range(len(commands)):
        i=commands[c][0]-1
        j=commands[c][1]
        k=commands[c][2]-1
        temp=array[i:j]
        temp.sort()
        answer.append(temp[k])
    return answer
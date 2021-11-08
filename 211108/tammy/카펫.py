def solution(brown, yellow):
    width = 0   #가로
    height = 0  #세로


    for i in range(1,yellow+1):
        if yellow % i == 0 :
            if i >= yellow//i:         # 세로보다 가로가 길때 리스트에 넣도록 함
                width = i               # yellow의 너비
                height = yellow//i     # yellow의 높이
                # print(width, height)
                if brown == (width*2)+(height*2)+4 :
                    return [width+2, height+2]



print(solution(10,2))
print(solution(24,24))
def solution(number, k):
    number_list = list(map(int, number))
    cnt = 0
    i=0
    answer =''
    while cnt < k:
        compare_list = number_list[i+1:i+k-cnt+1]
        # print(number_list[i+1:i+k-cnt+1])
        if i == len(number)-1 : 
            i+=1
            break
        elif number_list[i] < max(compare_list) :
            # number_list[i] = -1
            i+=1
            cnt += 1
        else : 
            answer += str(number_list[i])
            i+=1

    # print(number_list)
    
    answer +=''.join(map(str,number_list[i:]))
    return answer[:len(number)-k]

print(solution("10000", 4))
print(solution("4177252841", 4))
print(solution("1231234", 3))
print(solution("1924", 2))

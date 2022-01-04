def solution(phone_book):
    answer=True
    phone_book.sort()
    #문자열 정렬 '12','123','13' -> '12','123','13'
    #숫자 정렬 12,123,13-> 12,13,123
    for i in range(len(phone_book)-1):
        l_1=len(phone_book[i])
        l_2=len(phone_book[i+1])
        if l_1<l_2 and  phone_book[i]==phone_book[i+1][:l_1]:
            answer=False
        elif phone_book[i][:l_2]==phone_book[i+1]:
            answer=False
        if not answer:
            break
    return answer
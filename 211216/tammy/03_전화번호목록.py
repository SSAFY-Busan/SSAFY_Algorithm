def solution(phone_book):
    # 유효성 검사 3 4 fail
    # phone_book.sort(key=len)

    # for i in range(len(phone_book)-1):
    #     for j in range(i+1, len(phone_book)):
    #         print(phone_book[i][0],phone_book[j][0])
    #         if phone_book[i] == phone_book[j][:len(phone_book[i])] :
    #             return False

    # 길이로 정렬하지 말고, 문자열 자체로 정렬하면 사전순으로 정렬이 되므로 앞뒤만 비교하면 된다.
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        # 접두사라서 무조건 앞에있는 걸로 체크해야하는데, 접두사가 아닌경우도 in을 쓰면 체크해버리기때문에
        if phone_book[i] in phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True

# print(solution(["119", "97674223", "1195524421"]))
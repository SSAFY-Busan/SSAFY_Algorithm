# phone_book = ["119", "97674223", "1195524421"]
phone_book = ["123","456","789"]
# phone_book = ["12","123","1235","567","88"]

def solution(phone_book):
    phone_book.sort()
    for start, end in zip(phone_book[:-1], phone_book[1:]):
        # 테스트 케이스 13번이 통과가 안되서 찾아봄(startswith)
        # if start in end:
        if end.startswith(start):
            return False
    return True

###################################
# 해쉬 배운거 찾아봄
# def solution(phone_book):
#     answer = True
#     hash = {}
#     for phone in phone_book:
#         hash[phone] = 1
#     # print(hash)
#     for phone in phone_book:
#         # print(phone)
#         word = ""
#         for number in phone:
#             # print(number)
#             word += number
#             # 안에 있고
#             if word in hash and word != phone:
#                 answer = False
#     return answer

# print(solution(phone_book))

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = ''.join(numbers)
    if len(answer) == answer.count('0'):
        answer = '0'
    return answer

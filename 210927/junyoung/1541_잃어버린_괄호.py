# 잃어버린 괄호

# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다.
# 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.


sik = input().split('-')         # - 를 기준으로 나눠서 받기
in_sik = []                      #
for i in sik:                    # 식을 반복해서
    num = i.split('+')           # + 를 기준으로 나누기
    in_sik.append(num)           # 를 다시 저장
ans = []                         # 정답 리스트
for i in in_sik:                 # + 로 나눈 리스트를 반복해서
    hap = 0                      # 더할값
    for j in i:                  # 각각을 다시 반복해서
        hap += int(j)            # int 로 바꿔서 더하기
    ans.append(hap)              # 정답 리스트에 추가
for i in range(1, len(ans)):     # 첫번째 인덱스에서 다빼야하니깐 1부터 반복
    ans[0] -= ans[i]             # 0번부터 빼기
# print(sik)
# print(in_sik)
print(ans[0])


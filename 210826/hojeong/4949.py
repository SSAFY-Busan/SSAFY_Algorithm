#균형잡힌 세상
while 1:
    text=input()
    if text=='.': # . 하나를 입력받으면 반복문 종료
        break
    stack=[]
    for i in text:
        if i=='('or i=='[':
            stack.append(i)
        elif i==')':
            if stack:
                if stack[-1]=='(':
                    stack.pop() #'(' 제거
                else:
                    print('no')
                    break
            else: #스택이 비어있는데 닫는 괄호가 들어오면
                print('no')
                break
        elif i==']':
            if stack:
                if stack[-1]=='[':
                    stack.pop()
                else:
                    print('no')
                    break
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')
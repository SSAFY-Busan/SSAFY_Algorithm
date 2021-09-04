#문자열
def myDif(lst1,lst2): #lst1:A lst:B
    n=len(lst1)+pass_zone #len(lst2)-(len(lst2)-len(lst1)-pass_zone)
    result=0
    for i in range(pass_zone,n):
        if lst1[i-pass_zone]!=lst2[i]:
            result+=1
    return result

A,B=input().split()
a=len(A)
b=len(B)
min_cnt=a
for i in range(b-a+1): # i일때 앞에 알파벳 추가 i개 뒤에 추가 길이 차이-i
    pass_zone=i
    temp=myDif(A,B)
    if min_cnt>temp:
        min_cnt=temp
print(min_cnt)
#단어 정렬

N=int(input())
words=[0]*N
for i in range(N):
    words[i]=input()
words=list(set(words)) # 같은 단어가 여러번 입력된 경우에는 한번씩만 출력
l=len(words)

for i in range(l-1):
    for j in range(i+1,l):
        if len(words[i])>len(words[j]):
            words[i],words[j]=words[j],words[i]
        elif len(words[i])==len(words[j]):
            if words[i]>words[j]:
                words[i],words[j]=words[j],words[i]

print(*words,sep='\n')
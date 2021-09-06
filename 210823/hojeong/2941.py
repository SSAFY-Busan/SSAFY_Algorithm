#크로아티아 알파벳
change=['c=','c-','dz=','d-','s=','z=','lj','nj']
word=input()
l=len(word)
cnt=0
for i in change:
    cnt+=word.count(i)
print(l-cnt) #길이에서 변경 알파벳 갯수 만큼 빼주면 크로아티아 알파벳 개수

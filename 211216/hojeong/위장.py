clothes=[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
check={}
for a,b in clothes:
    if check.get(b):
        check[b].append(a)
    else:
        check[b]=[a]
total = 1
for i in check:
    total *= len(check[i]) + 1
print(total-1)
print(check)
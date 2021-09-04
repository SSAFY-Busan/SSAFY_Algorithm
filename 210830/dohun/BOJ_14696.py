N = int(input()) # 라운드 수
for game in range(N):
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))

    a_num = a_lst[0] # 개수
    b_num = b_lst[0] # 개수
    a_lst = a_lst[1:]
    b_lst = b_lst[1:]

    if a_lst.count(4) > b_lst.count(4):
        print("A")
    elif b_lst.count(4) > a_lst.count(4):
        print("B")
    else:
        if a_lst.count(3) > b_lst.count(3):
            print("A")
        elif b_lst.count(3) > a_lst.count(3):
            print("B")
        else:
            if a_lst.count(2) > b_lst.count(2):
                print("A")
            elif b_lst.count(2) > a_lst.count(2):
                print("B")
            else:
                if a_lst.count(1) > b_lst.count(1):
                    print("A")
                elif b_lst.count(1) > a_lst.count(1):
                    print("B")
                else:
                    print("D")

while True: # test case 정의 되어 있지 않음
    try:
        A, B = map(int, input().split(" "))
        print(A+B)
    except:
        break
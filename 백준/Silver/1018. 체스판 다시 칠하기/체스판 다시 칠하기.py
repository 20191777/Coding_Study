def main():
    global board
    n, m = map(int, input().split())   # n : y, m : x
    board = []

    # 체스판
    for _ in range(n):
        board.append(list(input().rstrip()))


    result = min(cut_board(n, m))
    print(str(result)[1:-1])   

def cut_board(n, m):
    ans = []
    for i in range(n-7):
        for j in range(m-7):
            ans.append(find(i, j))
    return ans

def find(n, m):
    cnt = []
    cnt_w = 0
    cnt_b = 0
    for i in range(n, n+8):
        for j in range(m, m+8):   
            if((i+j)%2 == 0):
                if board[i][j] != 'W':
                    cnt_w+=1
                if board[i][j] != 'B':
                    cnt_b+=1    
            else:
                if board[i][j] != 'B':
                    cnt_w+=1
                if board[i][j] != 'W':
                    cnt_b+=1 
    cnt.append(min(cnt_w, cnt_b))
    return cnt

if __name__ == "__main__":
    main()
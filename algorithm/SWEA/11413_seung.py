T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    board = [0, 0, 0, 0]
    for col in range(N):
        for row in range(M):
            if arr[col][row] == '#':
                if (col + row) % 2 == 0: # #짝수
                    board[0] += 1
                elif (col + row) % 2 == 1: # #홀수
                    board[1] += 1


            elif arr[col][row] == '.':
                if (col + row) % 2 == 0: # .짝수
                    board[2] += 1
                elif (col + row) % 2 == 1: # .홀수
                    board[3] += 1



    # match가 되는 4가지 경우를 비교한다.

    if (board[0]>0 and board[1]>0) or (board[2]>0 and board[3]>0) or board[0] :
        answer = 'impossible'
    else:
        answer = 'possible'

    print(board[0], board[1], board[2], board[3])
    print(f'#{tc} {answer}')
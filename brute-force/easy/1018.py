#https://www.acmicpc.net/problem/1018 체스판 다시 칠하기 
#문제보자마자 바로 생각이 났다. Computing power 를 사용하는 데 익숙해서 그런 듯하다. (과거에 소수 구하기와 비슷한 느낌이 든다.)

import sys

N, M = map(int, input().split())

chess_board1 = [['W' if (i+j) % 2 == 0 else 'B' for j in range(8)] for i in range(8)]
chess_board2 = [['B' if (i+j) % 2 == 0 else 'W' for j in range(8)] for i in range(8)]
chess_board = []

cnt = []
for i in range(N):
    chess_board.append(sys.stdin.readline().rstrip())

for i in range(N-7):
    for j in range(M-7):
        tmp_cnt = 0
        m=0
        for k1 in range(i,i+8):
            n=0
            for k2 in range(j,j+8):
                if chess_board[k1][k2] != chess_board1[m][n]:
                    tmp_cnt += 1
                n += 1
            m += 1
        cnt.append(tmp_cnt)

for i in range(N-7):
    for j in range(M-7):
        tmp_cnt = 0
        m=0
        for k1 in range(i,i+8):
            n=0
            for k2 in range(j,j+8):
                if chess_board[k1][k2] != chess_board2[m][n]:
                    tmp_cnt += 1
                n += 1
            m += 1
        cnt.append(tmp_cnt)

print(min(cnt))
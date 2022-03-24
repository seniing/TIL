import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    count = 0

    # 행 우선 순회
    answer1 = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                count += 1
                if count > answer1:
                    answer1 = count
            else:
                count = 0

    # 열 우선 순회
    answer2 = 0
    for j in range(M):
        for i in range(N):
            if arr[i][j] == 1:
                count += 1
                if count > answer1:
                    answer1 = count
            else:
                count = 0

    if answer1 > answer2:
        print(f'#{tc} {answer1}')
    else:
        print(f'#{tc} {answer2}')
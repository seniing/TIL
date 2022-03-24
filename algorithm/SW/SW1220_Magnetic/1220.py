import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        m = 0
        for j in range(N):
            if arr[j][i] == 1:               # N극 아래로 이동
                m = 1
            elif arr[j][i] == 2 and m == 1:  # N극 아래로 가다가 S극을 만남
                cnt += 1
                m = 0
    print(f'#{tc} {cnt}')
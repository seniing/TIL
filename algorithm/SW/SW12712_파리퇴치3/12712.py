import sys
sys.stdin = open('in1.txt')

T = int(input())
for tc in range(1, T+1):
    # N*N 배열, M은 분사거리
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # + 찾기
    max_cnt1 = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            cnt += arr[i][j]
            for k in range(1, M):
                for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    ni, nj = i+di*k, j+dj*k
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            if cnt > max_cnt1:
                max_cnt1 = cnt

    # x 찾기
    max_cnt2 = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            cnt += arr[i][j]
            for k in range(1, M):
                for di, dj in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
                    ni, nj = i + di * k, j + dj * k
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            if cnt > max_cnt2:
                max_cnt2 = cnt

    if max_cnt1 > max_cnt2:
        print(f'#{tc} {max_cnt1}')
    else:
        print(f'#{tc} {max_cnt2}')
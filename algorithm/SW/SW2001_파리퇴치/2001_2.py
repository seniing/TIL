import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N*N 배열, M*M 파리채
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_s = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for x in range(M):
                for y in range(M):
                    s += arr[i+x][j+y]
            if s > max_s:
                max_s = s

    print(f'#{tc} {max_s}')

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    # N : 상자의 개수, Q : 횟수
    N, Q = map(int, input().split())
    box = [0] * N
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            box[j] = i + 1
    print(f'#{tc}', *box)
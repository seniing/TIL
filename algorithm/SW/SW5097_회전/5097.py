import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    for i in range(M):
        queue.append(queue.pop(0))
    print(f'#{tc} {queue[0]}')
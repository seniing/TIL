import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 버스노선의 개수
    bus = []
    answer = [0] * 5000
    for i in range(N):
        a, b = map(int, input().split())
        for j in range(a-1, b):
            answer[j] += 1

    n = int(input())  # 정류장의 개수
    station = [int(input()) for _ in range(n)]  # 정류장의 번호
    result = []
    for i in station:
        result.append(answer[i-1])
    print(f'#{tc}', *result)



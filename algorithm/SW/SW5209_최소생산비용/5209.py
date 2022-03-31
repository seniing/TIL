import sys
sys.stdin = open('sample_input.txt')


def f(n, total):
    global answer
    # 공장을 다 정했을 경우
    if n == N:
        # 생산비용이 answer 보다 작으면 answer 변경
        if total < answer:
            answer = total
            return

    # 생산비용이 answer 보다 크면 최소 생산비용이 아님
    if total > answer:
        return

    for i in range(N):
        # 방문하지 않은 공장일 때
        if visited[i] == 0:
            # 방문한 공장으로 변경
            visited[i] = 1
            # 그 공장의 생산 비용을 더하고 다음 공장으로 이동
            f(n+1, total + arr[n][i])
            # 공장을 다시 선택할 수 있도록 방문하지 않은 공장으로 변경
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    answer = 1500

    f(0, 0)
    print(f'#{tc} {answer}')
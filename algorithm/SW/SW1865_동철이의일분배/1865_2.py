import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # dp 리스트 초기화
    dp = [-1] * (1 << N)
    answer = 0


    def dfs(now, visited):
        # visited == 1 << N - 1 이면 모든 곳을 방문했다는 뜻이므로 return
        if visited == (1 << N) - 1:
            return 1
        # dp가 -1이 아니면 방문을 했다는 뜻이므로 return
        if dp[visited] != -1:
            return dp[visited]
        # dp는 곱해질 것이므로 초기값 1
        dp[visited] = 1
        for i in range(N):
            # 방문했으면 continue
            if visited & 1 << i:
                continue
            # 방문해야한다면
            else:
                # 현재값과 진행값 중 최댓값을 가져가기
                dp[visited] = max(dp[visited], dfs(now + 1, visited | (1 << i)) * arr[now][i])
        return dp[visited]

    answer = dfs(0, 0)
    # 현재 answer는 모든 원소의 곱들의 최댓값이므로 이를 100^(N)으로 나눠주고 100을 곱해주는 과정을 진행하야함
    answer = round(answer / (100 ** (N - 1)), 6)
    print(f'#{tc} {answer:.6f}')

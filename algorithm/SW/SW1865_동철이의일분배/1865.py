import sys
sys.stdin = open('input.txt')


def percent(people, result):
    global answer

    # 모든 성공확률을 곱한 경우
    if people == N:
        # 확률이 answer 보다 크다면 answer 변경
        if result > answer:
            answer = result
            return

    # 확률이 answer 보다 작아지면 더 이상 커질 일이 없기 때문에 탐색 종료
    if result <= answer:
        return

    for i in range(N):
        # 주어진 일이 아닐때
        if visited[i] == 0:
            # 방문체크
            visited[i] = 1
            # 확률 값에 주어진 일을 성공할 확률 곱하고 다음 사람으로 이동
            percent(people+1, result * arr[people][i] * 0.01)
            # 주어진 일을 선택할 수 있도록 방문 체크 해제
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    answer = 0

    percent(0, 1)
    print(f'#{tc} {answer*100:.6f}')

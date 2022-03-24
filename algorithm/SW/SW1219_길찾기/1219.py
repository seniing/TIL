import sys
sys.stdin = open('input.txt')


def dfs(v):
    stack = [v]
    while stack:
        v = stack.pop()
        # v가 도착지점 이면 1을 반환
        if v == 99:
            return 1
        # v가 갈수 있는 길 모두를 stack 에 쌓기
        if second[v]:
            stack.append(second[v])
            stack.append(first[v])
        elif first[v]:
            stack.append(first[v])
    return 0


T = 10
for tc in range(1, T+1):
    # 테스트케이스번호, 순서쌍의 개수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    first = [0]*100
    second = [0]*100

    for i in range(0, M*2, 2):
        # 갈 길이 있는 경우에 first 에 저장
        # first 에 값이 있는 경우에는 second 에 저장
        if first[arr[i]] == 0:
            first[arr[i]] += arr[i + 1]
        else:
            second[arr[i]] += arr[i + 1]

    print(f'#{tc} {dfs(0)}')
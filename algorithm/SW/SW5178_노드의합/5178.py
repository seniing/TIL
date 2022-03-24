import sys
sys.stdin = open('sample_input.txt')


def maketree(v):
    # 주어진 값보다 노드번호가 작으면 존재
    if v <= (N - M):
        maketree(v*2)
        maketree(v*2 + 1)
        # 자식이 둘다 있을 때
        try:
            tree[v] = tree[v * 2] + tree[v * 2 + 1]
        # 자식이 하나만 있을 때
        except:
            tree[v] = tree[v * 2]


T = int(input())
for tc in range(1, T+1):
    # N : 노드 개수, M : 리프 노드 개수, L : 값을 출력할 노드 번호
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for i in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num

    maketree(1)
    print(f'#{tc} {tree[L]}')
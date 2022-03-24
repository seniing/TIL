import sys
sys.stdin = open('sample_input.txt')


def maketree(v):
    global num
    # 주어진 값보다 노드번호가 작으면 존재
    if v <= N:
        maketree(v*2)
        # 노드번호에 숫자 넣기
        tree[v] = num
        num += 1
        maketree(v*2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 1

    maketree(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')

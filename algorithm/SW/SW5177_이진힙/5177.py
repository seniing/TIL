import sys
sys.stdin = open('sample_input.txt')


# 이진 힙 만들기
def enq(n):
    global last
    last += 1
    tree[last] = n  # 완전이진트리 유지
    c = last  # 새로 추가된 정점을 자식으로
    p = c // 2  # 완전이진트리에서의 부모 정점 번호

    while p >= 1 and tree[p] > tree[c]:  # 부모가 있고, 부모의 값이 더 크면 교환
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N+1)
    last = 0
    answer = 0

    for i in arr:
        enq(i)

    a = N // 2  # 부모의 노드 번호
    while a > 0:
        answer += tree[a]
        a //= 2
    print(f'#{tc} {answer}')



import sys
sys.stdin = open('sample_input.txt')


def inorder(v):
    global count
    # 노드가 있으면 count += 1
    if v:
        count += 1
        inorder(ch1[v])
        inorder(ch2[v])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1

    # 부모번호를 인덱스로 자식번호 저장
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    for i in range(E):
        p, c = arr[i*2], arr[i*2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    count = 0
    inorder(N)
    print(f'#{tc} {count}')
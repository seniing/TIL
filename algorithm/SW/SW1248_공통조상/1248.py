import sys
sys.stdin = open('input.txt')


def search_anc(v):
    anc = []
    while par[v] != 0:
        anc.append(par[v])
        v = par[v]
    return anc


def preorder(v):
    global count
    if v:
        count += 1
        preorder(ch1[v])
        preorder(ch2[v])
    return count


T = int(input())
for tc in range(1, T+1):
    # V : 정점의 수, E : 간선의 수, v1/v2 : 2개의 정점
    V, E, v1, v2 = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0

    # 부모번호를 인덱스로 자식번호 저장
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    for i in range(E):
        if ch1[arr[i*2]] == 0:  # 아직 자식이 없는 경우
            ch1[arr[i*2]] = arr[i*2 +1]
        else:
            ch2[arr[i*2]] = arr[i*2 +1]

    # 자식 번호를 인덱스로 부모번호 저장
    par = [0] * (V+1)
    for i in range(E):
        par[arr[i*2 + 1]] = arr[i*2]

    # 같은 조상찾기
    a = []
    for i in search_anc(v1):
        for j in search_anc(v2):
            if i == j:
                a.append(i)
    print(f'#{tc} {a[0]} {preorder(a[0])}')

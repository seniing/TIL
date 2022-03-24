import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)  # 값을 저장할 tree
    ch1 = [0] * (N+1)   # 왼쪽 자식
    ch2 = [0] * (N+1)   # 오른쪽 자식

    for i in range(N):
        arr = list(input().split())
        idx = int(arr[0])           # index 값
        tree[idx] = arr[1]          # tree 에 넣기
        if len(arr) == 4:           # 자식이 있으면 자식의 index 넣기
            ch1[idx] = int(arr[2])
            ch2[idx] = int(arr[3])

    # 뒤에서 부터 계산 : 왼쪽 자식 '연산자' 오른쪽 자식
    for i in range(N, 0, -1):
        if tree[i] == '+':
            tree[i] = int(tree[ch1[i]]) + int(tree[ch2[i]])
        elif tree[i] == '-':
            tree[i] = int(tree[ch1[i]]) - int(tree[ch2[i]])
        elif tree[i] == '/':
            tree[i] = int(tree[ch1[i]]) / int(tree[ch2[i]])
        elif tree[i] == '*':
            tree[i] = int(tree[ch1[i]]) * int(tree[ch2[i]])

    print(f'#{tc} {int(tree[1])}')
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())   # 교실바닥 : 20*N
    n = N//10          # N은 10의 배수
    arr = [0, 1, 3]    # N:0 -> 0, N:10 -> 1, N:20 -> 3
    # 10 <= N <-300
    for i in range(3, 301):
        # arr[i] = arr[i-1] * arr[1] + arr[i-2] * (arr[2]-1)
        # (arr[2]-1) -> 세워져 있는 종이가 arr[i-1]과 겹친다
        a = arr[i-1] + arr[i-2]*2
        arr.append(a)
    print(f'#{tc} {arr[n]}')
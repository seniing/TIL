import sys
sys.stdin = open('sample_input.txt')

# 버블 정렬으로 오름차순 정렬
def special(arr):
    for i in range(10):
        minmax = i
        if i % 2:
            for j in range(i, N):
                if arr[minmax] > arr[j]:
                    minmax = j
        else:
            for j in range(i, N):
                if arr[minmax] < arr[j]:
                    minmax = j
        arr[i], arr[minmax] = arr[minmax], arr[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 정수의 개수
    arr = list(map(int, input().split()))  # 정수 list
    special(arr)

    print(f"#{tc}", end=' ')
    print(*arr[:10])



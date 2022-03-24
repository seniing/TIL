import sys
sys.stdin = open('sample_input.txt')

# 버블 정렬으로 오름차순 정렬
def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 정수의 개수
    arr = list(map(int, input().split()))  # 정수 list

    new_list = BubbleSort(arr, N)
    answer = []
    end = N - 1
    start = 0
    # 큰 값, 작은 값 번갈아 가면서 넣어주기
    for i in range(5):
        answer.append(str(new_list[end]))
        answer.append(str(new_list[start]))
        end = end - 1
        start = start + 1

    print(f"#{tc} {' '.join(answer)}")



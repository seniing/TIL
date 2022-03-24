import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # 원소의 개수, 원소의 합
    arr_A = [i for i in range(1, 13)]
    n = len(arr_A)  # 12
    answer = 0

    # 부분집합 구하기
    for i in range(1 << n):
        sub_A = []
        for j in range(n):
            if i & (1 << j):
                sub_A.append(arr_A[j])

        # 부분집합의 원소 개수가 N일 때 원소들의 합 구하기
        if len(sub_A) == N:
            sum_A = 0
            for k in sub_A:
                sum_A += k
            if sum_A == K:
                answer += 1

    print(f'#{tc} {answer}')


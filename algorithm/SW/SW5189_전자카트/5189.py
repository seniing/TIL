import sys
sys.stdin = open('sample_input.txt')


def f(n, k):
    global answer

    result = 0  # 배터리 소비량
    if n == k:                               # 순열이 완성 되었을 때
        c = [1]+p+[1]                        # 시작과 끝 값은 항상 1
        for i in range(len(c)-1):
            # 1-2-1 : arr[1][2] + arr[2][1]
            # index : arr[0][1] + arr[1][0]
            result += arr[c[i]-1][c[i+1]-1]
        # 최소 소비량 구하기
        if result < answer:
            answer = result

    else:
        for i in range(k):    # used 에서 사용하지 않은 숫자 검색
            if used[i] == 0:  # 앞에서 사용하지 않은 숫자인 경우
                used[i] = 1   # 사용함으로 표시
                p[n] = a[i]   # p[n] 결정
                f(n+1, k)
                used[i] = 0   # a[i]를 다른 위치에서 사용할 수 있도록 함
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = [0] * (N-1)
    used = [0] * (N-1)
    a = [i for i in range(2, N+1)]  # 모든 값은 2부터 N까지
    answer = 9999999999
    f(0, N-1)
    print(f'#{tc} {answer}')
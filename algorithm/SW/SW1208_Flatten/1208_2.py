import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, 11):
    N = int(input())  # 덤프 횟수
    h_list = list(map(int, input().split()))

    def h_max():
        h_max = h_list[0]
        num_max = 0
        for i in range(len(h_list)):
            if h_list[i] > h_max:
                h_max = h_list[i]
                num_max = i
        return num_max

    def h_min():
        h_min = h_list[0]
        num_min = 0
        for i in range(len(h_list)):
            if h_list[i] < h_min:
                h_min = h_list[i]
                num_min = i
        return num_min

    for i in range(N):
        h_list[h_max()] -= 1
        h_list[h_min()] += 1

    print(f'#{tc} {h_list[h_max()] - h_list[h_min()]}')


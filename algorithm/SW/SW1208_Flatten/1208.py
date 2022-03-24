import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, 11):
    N = int(input())  # 덤프 횟수
    h_list = list(map(int, input().split()))  # 상자들의 높이

    # 덤프 횟수만큼 반봅
    for i in range(N):
        h_max = h_list[0]
        h_min = h_list[0]
        num_max = 0  # 가장 높은 상자의 index 값
        num_min = 0  # 가장 낮은 상자의 index 값
        for h in range(len(h_list)):
            if h_list[h] > h_max:
                h_max = h_list[h]
                num_max = h
            if h_list[h] < h_min:
                h_min = h_list[h]
                num_min = h
        # 가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기기        
        h_list[num_max] -= 1
        h_list[num_min] += 1
    
    # 덤프 후 최고점과 최저점의 차이 구하기
    max_value = h_list[0]
    min_value = h_list[0]
    for i in h_list:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i

    print(f'#{tc} {max_value - min_value}')

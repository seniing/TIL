import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 카드 장 수
    arr = list(map(int, input()))  # 카드 list

    count_list = [0 for i in range(10)]  # 숫자의 카드 장수를 저장할 list

    # 카드 list 숫자 값 = count_list index 값
    # 숫자가 나올 때마다 그 자리에 1씩 더하기
    for i in arr:
        count_list[i] += 1

    # count_list 중 가장 큰 값 찾기
    max_count = count_list[0]
    for j in range(10):
        if count_list[j] >= max_count:
            max_count = count_list[j]
            k = j  # 가장 큰 값의 숫자 불러오기

    print(f'#{tc} {k} {max_count}')
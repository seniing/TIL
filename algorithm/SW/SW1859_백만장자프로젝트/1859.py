import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # N일
    price_list = list(map(int, input().split()))

    max_price = price_list[N-1]   # 처음 max 값을 list 의 끝 값으로 설정
    sum_price = 0                 # 이익을 저장해 줄 값
    for i in range(N-2, -1, -1):  # 뒤에서 2번재 값부터 비교하기
        # max_price 의 값보다 작으면 이익 = 큰 값 - 작은값
        # max_price 값은 그대로 유지
        if price_list[i] < max_price:
            sum_price += max_price - price_list[i]
        # max_price 안의 값보다 들어오는 값이 더 크면 그 값을 max_price
        else:
            max_price = price_list[i]
    print(f'#{tc} {sum_price}')
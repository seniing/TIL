import sys
sys.stdin = open('sample_input.txt')


def charge(num, count):
    global answer
    # 종점에 도착 했을 경우
    if num >= N:
        # 배터리 교환 횟수가 answer 보다 작으면 answer 변경
        if count < answer:
            answer = count
            return

    # 종점에 도착하지 않았을 경우 -> 배터리 교환 +1
    count += 1
    # 지금 까지의 교환 횟수가 answer 보다 크면 최소한의 교환횟수가 아님
    if count > answer:
        return

    total = arr[num]  # 배터리로 갈 수 있는 거리
    for i in range(total, 0, -1):
        charge(num+i, count)


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    answer = 10000

    charge(1, 0)
    print(f'#{tc} {answer-1}')
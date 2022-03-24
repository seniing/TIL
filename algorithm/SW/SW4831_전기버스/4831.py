import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    # K = 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N = 정류장의 개수
    # M = 충전기가 설치된 정류장의 개수
    K, N, M = map(int, input().split())
    # arr = 충전기가 설칟된 정류장
    arr = list(map(int, input().split()))

    # 정류장 위치 list
    charge_list = [0 for i in range(N+1)]
    for i in arr:
        charge_list[i] += 1

    location = 0  # 위치
    count = 0  # 충전 횟수

    while True:
        location += K  # 출발지에서 충전
        # 종점에 도착하면 while문 종료
        if location >= N:
            break
        # 충전소에서 충전을 하면 충전 횟수 +1, 위치 바꿔주기
        for i in range(location, location-K, -1):
            if charge_list[i] == 1:
                count += 1
                location = i
                break
        # 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우
        else:
            count = 0
            break

    print(f'#{tc} {count}')

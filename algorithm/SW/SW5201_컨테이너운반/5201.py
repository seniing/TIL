import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 화물의 무게와 트럭의 적재용량 정렬
    w = sorted(w)
    truck = sorted(truck)

    answer = 0
    # 뒤에서부터 꺼내서 확인
    while truck and w:
        # 트럭의 적재용량
        a = truck.pop()
        while w:
            # 화물의 무게
            b = w.pop()
            # 트럭이 화물을 실을 수 있다면 답에 화물의 무게 추가가
            if a >= b:
                answer += b
                break
    print(f'#{tc} {answer}')
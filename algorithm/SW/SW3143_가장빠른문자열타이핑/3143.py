import sys
sys.stdin = open('sample_input.txt')


def BruteForce(p, t):
    count = 0
    M = len(p)  # 찾을 패턴의 길이
    N = len(t)  # 전체 텍스트의 길이
    i = 0
    count = 0
    while i < N:  # 전체 텍스트의 길이가 넘어가면 while 문 종료
        # 패턴의 첫 번재 문자와 텍스트의 첫 번째 문자가 같다면 첫 번째 문자를 시작으로 패턴과 같은지 찾기
        if t[i] == p[0]:
            #  패턴과 텍스트 안의 값이 같다면 타이핑 횟수 +1, i는 패턴의 길이만큼 이동
            if t[i:i+M] == p:
                count += 1
                i += M
            # 같지 않다면 타이밍 횟수 +1, i는 한칸 이동
            else:
                count += 1
                i += 1
        else:
            count += 1
            i += 1
    return count


T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    print(f'#{tc} {BruteForce(B, A)}')
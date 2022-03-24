import sys
sys.stdin = open('sample_input.txt')


def search_pt(p, t):
    M = len(p)  # 찾을 패턴의 길이
    N = len(t)  # 전체 텍스트의 길이
    for i in range(N-M+1):  # 전체 텍스트의 길이에서 찾을 패턴의 길이를 뺀 만큼까지
        for j in range(M):
            if t[i] != p[j]:  # 서로 문자가 다르면 for 문 종료
                break
            else:  # 서로 문자가 같으면 그 다음 문자 비교
                i += 1
                j += 1
        if j == M:  # 패턴 끝까지 비교가 끝났다면 = 패턴과 일치하는 부분이 텍스트에 존재
            return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    p = input()
    t = input()

    print(f'#{tc} {search_pt(p, t)}')

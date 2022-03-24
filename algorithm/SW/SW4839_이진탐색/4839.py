import sys
sys.stdin = open('sample_input.txt')


# 몇 번 탐색하는지 세는 함수
def page_search(Pi, P):  # Pi = 찾을 페이지 / P = 전체 페이지
    count = 0
    start = 1  # 처음 시작은 1페이지 부터
    while True:
        center = (start + P) // 2  # 중간 페이지를 찾는 식
        if Pi == center:  # 찾을 페이지와 중간 페이지가 같다면 count 값 출력
            return count
        # 찾을 페이지가 중간 페이지 보다 작다면 페이지를 기준으로 왼쪽영역의 중간페이지 찾기
        elif Pi < center:
            P = center  # center = (start + center) // 2
        # 찾을 페이지가 중간 페이지 보다 크다면 페이지를 기준으로 오른쪽영역의 중간페이지 찾기
        elif Pi > center:
            start = center  # center = (center + P) // 2
        count += 1


T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    answer = ''
    if page_search(Pa, P) < page_search(Pb, P):
        answer = 'A'
    elif page_search(Pa, P) > page_search(Pb, P):
        answer = 'B'
    else:
        answer = 0

    print(f'#{tc} {answer}')

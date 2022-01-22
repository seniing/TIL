import json


def max_score(scores):
    pass
    # 여기에 코드를 작성합니다.
    
    x = scores[0] # 비교를 위해 scres 첫 번째 값을 x에 대입
    for i in scores: # scores의 값 모두 반복
        if i > x: # scores에 i값이 x보다 크다면 x에 i를 대입
            x = i
    return x 


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90

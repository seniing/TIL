import json


def over(scores):
    pass
    # 여기에 코드를 작성합니다.
    scores_count = 0 # 조건에 맞는 과목의 개수를 저장할 값 생성
    for i in scores: 
        if i >= 60: # 만약 scores 안의 점수가 60 이상이라면
            scores_count += 1 # scores_count 에 1씩 더하기
    return scores_count



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3

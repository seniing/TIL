import json


def max_score(scores):
    x = scores[0]
    for i in scores:
        if i > x:
            x = i
    return x


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90

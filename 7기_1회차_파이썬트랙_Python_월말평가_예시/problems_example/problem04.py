import json


def turn(temperatures):
    pass
    # 여기에 코드를 작성합니다.

    max_list = [] # macimum의 값이 들어갈 list
    min_list = [] # minimum의 값이 들어갈 list
    for day_list in temperatures:
        max_list.append(day_list[0]) # temperatures 안의 day_list 중 1번째 값을 max_list에 추가
        min_list.append(day_list[1]) # temperatures 안의 day_list 중 2번째 값을 min_list에 추가

    max_min_dict = {} # 새로운 dict
    max_min_dict = {'maximum': max_list, 'minimum': min_list}

    return max_min_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperatures = [
        [9, 3],
        [9, 0],
        [11, -3],
        [11, 1],
        [8, -3],
        [7, -3],
        [-4, -12]
    ]
    print(turn(temperatures)) 
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4], 
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }

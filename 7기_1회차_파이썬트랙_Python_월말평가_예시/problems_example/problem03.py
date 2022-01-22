import json


def menu_count(restorant):
    pass
    # 여기에 코드를 작성합니다.
    
    menus = restorant.get('menus') # menus의 값 가져오기
    my_count = 0 # 메뉴의 개수를 저장하기 위한 값 생성
    for i in menus:
        my_count += 1 # munus에 값이 있다면 my_count에 1씩 더하기
    return my_count


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    restorant = {
        "id": 11,
        "user_rating": 5.5,
        "name": "김밥나라",
        "menus": ["참치김밥", "치즈라면", "돈까스", "비빔밥"],
        "location": "서울특별시 강남구 역삼동 123-123"
    }
    print(menu_count(restorant)) # 4

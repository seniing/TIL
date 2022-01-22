import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    
    # # movies = [{}, {}, {}]
    # 1. id_list 만들기 / 2. id_list 영화의 상세정보 불러오기 / 3. id_revenue 가져와서 비교 - max 값 찾아서 title 출력
    
    # 1. id_list 만들기
    id_list = []
    for movie in movies:
        id_list.append(movie.get('id')) # id_list = [278, 238]

    # 2. id_list 영화의 상세정보 불러오기 
    # 3. id_revenue 가져와서 비교 - max 값 찾아서 title 출력
    max_rev = 0
    for id in id_list:
        # id값에 따른 json 파일 열기
        id_json = open(f'data/movies/{id}.json', encoding = 'utf-8')
        id_dict = json.load(id_json) #json 파일을 dict 형태로 변환
        id_revenue = id_dict.get('revenue') # revenue 값만 추출
        # revenue 값 끼리 비교해 높은 값을 max_rev에 저장
        if max_rev < id_revenue:
            max_rev = id_revenue
            max_rev_name = id_dict.get('title') # max_rev의 'title' 가져오기
            print(max_rev_name)
        
    return max_rev_name
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    
    # release_date
    # movies = [{}, {}, {}]
    # 1. id_list 만들기 / 2. id_list 영화의 상세정보 불러오기 / 3. release_data에서 12월에 개봉하는 영화 리스트 작성
    
    # 1. id_list 만들기
    id_list = []
    for movie in movies:
        id_list.append(movie.get('id')) # id_list = [278, 238]

    # 2. id_list 영화의 상세정보 불러오기 
    # 3. release_data에서 12월에 개봉하는 영화 리스트 작성
    dec_movie = ''
    dec_movie_list = []
    for id in id_list:
        # id값에 따른 json 파일 열기
        id_json = open(f'data/movies/{id}.json', encoding = 'utf-8')
        id_dict = json.load(id_json) #json 파일을 dict 형태로 변환
        id_date = id_dict.get('release_date') # release_date 값만 추출 
        date_mon = id_date[5:7] # 2022-01-21 에서 01만 추출 == 월만 추출
        if date_mon == '12': # 값이 12월 이라면
            dec_movie = id_dict.get('title') # 영화의 title 가져오기
            dec_movie_list.append(dec_movie) # 조건에 맞는 title을 list에 추가         
    
    return dec_movie_list
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
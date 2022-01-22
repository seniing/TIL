import json
from operator import ge
from pprint import pprint

from pyparsing import nested_expr


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.


    # # 1. movies : 필요한 정보만 가져오기 / 2. 추가 / 3. return
    # keys = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    # res_dict = {} # 새로만든 dict
    # for key in keys:
    #     if key == 'genre_ids':
    #         names = [] # [CRIME, DRAMA]
    #         ids = movie.get('genre_ids') # [18, 80]
    #         for genre in genres:
    #             if genre['id'] in ids: # genre의 'id'가 ids 안에 있는 'id' 값이라면
    #                 names.append(genre['name']) # 그 'id'의 'name' 추가
    #         res_dict['genre_names'] = names
    #     else:
    #         res_dict[key] = movie.get(key)

    # return res_dict
    


    # 1. 아이디와 장르 딕셔너리로 만들기 / 2. movie에서 id 값을 찾아 genre 찾기 / 3. 변환하여 추가하기
    #[{"id": 28, "name": "Action"] genres.json 형태
    genres_dict = {} # {28 : 'Action}
    for genre in genres:
        genres_dict[genre.get('id')] = genre.get('name') # geners에서 key => id, value => name으로 dict 생성
    
    genre_names = [] # ['Action' , 'Adventure] genre 이름 list 만들기
    genre_ids = movie.get('genre_ids') # movie에서 genre id만 가져오기
    for genre_id in genre_ids:
        genre_names.append(genres_dict[genre_id])

    # genre_ids -> genre_names
    new = {
        'genre_names': genre_names,
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'poster_path': movie.get('poster_path'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average'),
    }
    
    return new


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    # movie_total = []
    # for movie in movies:
    #     genres_dict = {}
    #     for genre in genres:
    #         genres_dict[genre.get('id')] = genre.get('name')
    #         # genre_dict = {28: 'Action', 12: 'Adventure', }
    #     genre_names = []
    #     genre_ids = movie.get('genre_ids')
    #     for genre_id in genre_ids:
    #         # genre_names += [genres_dict[genre_id]]
    #         genre_names.append(genres_dict[genre_id])

    #     new = {
    #         'genre_names': genre_names,
    #         'id': movie.get('id'),
    #         'overview': movie.get('overview'),
    #         'poster_path': movie.get('poster_path'),
    #         'title': movie.get('title'),
    #         'vote_average': movie.get('vote_average'),
    #     }
    #     movie_total.append(new)
    # return movie_total
    
    
        # 1. movies : 필요한 정보만 가져오기 / 2. 추가 / 3. return
    movie_total = []
    for movie in movies:
        keys = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
        res_dict = {} # 새로만든 dict
        for key in keys:
            if key == 'genre_ids':
                names = [] # [CRIME, DRAMA]
                ids = movie.get('genre_ids') # [18, 80]
                for genre in genres:
                    if genre['id'] in ids: # genre의 'id'가 ids 안에 있는 'id' 값이라면
                        names.append(genre['name']) # 그 'id'의 'name' 추가
                res_dict['genre_names'] = names
            else:
                res_dict[key] = movie.get(key)
        movie_total.append(res_dict)
    return movie_total
    
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
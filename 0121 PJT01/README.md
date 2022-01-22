# Project 01_Python을 활용한 데이터 수집:fire:

---

1. 목표
   - Python 기본 문법 실습
   - 파일 입출력에 대한 이해
   - 데이터 구조에 대한 분석과 이해
   - 데이터를 가공하고 JSON 형태로 저장

------



---

## problem_a 

- 제공되는 영화 데이터의 주요내용 수집
  - id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 정보만 가져온다.
  - dictionary로 반환하는 함수 movie_info

```
import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.  
    new = {
        'genre_ids': movie.get('genre_ids'),
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
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
```

```
import json
from pprint import pprint


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.  
    keys = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    new_dict = {}
    for key in keys:
        new_dict[key] = movie.get(key)
    
    return new_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
```



- **dict_name.get('key_name')** : dict_name에서 'key_name'에 할당된 값 가져오기
- new = {**'key'**: **dict_name.get('key_name')**}



---

## problem_b

- 제공되는 영화 데이터의 주요내용 수정
  - id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 정보만 가져온다.
  - genre_ids를 genre_names로 변환하여 dictionary에 추가하는 함수 movie_info

:heart: **1. 아이디와 장르 딕셔너리로 만들기 / 2. movie에서 id 값을 찾아 genre 찾기 / 3. 변환하여 추가하기**

```
import json
from operator import ge
from pprint import pprint

from pyparsing import nested_expr


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.

    #[{"id": 28, "name": "Action"] genres.json 형태
    genres_dict = {} # {28 : 'Action}
    for genre in genres:
    	# geners에서 key => id, value => name으로 dict 생성
        genres_dict[genre.get('id')] = genre.get('name') 
    
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
```

:heart: **1. movies : 필요한 정보만 가져오기 / 2. movie의 id 값에 맞는 genre name 추가 / 3. return**

```
import json
from operator import ge
from pprint import pprint

from pyparsing import nested_expr


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.
    
    keys = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    res_dict = {} # 새로만든 dict
    for key in keys: # 원하는 키의 값만 가져오기
        if key == 'genre_ids':
            names = [] # [CRIME, DRAMA]
            ids = movie.get('genre_ids') # [18, 80]
            for genre in genres:
                if genre['id'] in ids: # genre의 'id'가 ids 안에 있는 'id' 값이라면
                    names.append(genre['name']) # 그 'id'의 'name' 추가
            res_dict['genre_names'] = names
        else:
            res_dict[key] = movie.get(key)

    return res_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
```

- **new[key] = value** : Dictionary 만들기
- **list_name.append(dict_name['key_name'])** : List에 Dict에서 'key_name'에 할당된 값 추가하기

- **dict_name.get('key_name')** : dict_name에서 'key_name'에 할당된 값 가져오기

  

---

## problem_c

- 다중 데이터 분석 및 수정
  - 이전 단계의 함수 구조를 재사용 하여 영화 전체 정보를 수정하여 반환하는 함수 movie_info 

:heart: **이전 단계의 함수를 가져와서 반복문 돌려서 반환하기**

```
import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    movie_total = []
    for movie in movies:
        genres_dict = {}
        for genre in genres:
            genres_dict[genre.get('id')] = genre.get('name')
            # genre_dict = {28: 'Action', 12: 'Adventure', }
        genre_names = []
        genre_ids = movie.get('genre_ids')
        for genre_id in genre_ids:
            # genre_names += [genres_dict[genre_id]]
            genre_names.append(genres_dict[genre_id])

        new = {
            'genre_names': genre_names,
            'id': movie.get('id'),
            'overview': movie.get('overview'),
            'poster_path': movie.get('poster_path'),
            'title': movie.get('title'),
            'vote_average': movie.get('vote_average'),
        }
        movie_total.append(new)
    return movie_total
    
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```

```
import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
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
```



---

## problem_d

- 알고리즘을 통한 데이터 출력
  - 수익이 가장 높은 영화의 제목을 출력하는 함수 max_revenue

:heart: **1. id_list 만들기 / 2. id_list 영화의 상세정보 불러오기 / 3. revenue 비교 : max 값 찾아서 title 출력**

```
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
        
    return max_rev_name
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
```

- **json_name = open('folder_name/file_name.json', encodint='UTF8')** : json 파일 열기
- **json_dict = json.lead(json_name)** : json 파일을 dict 형태로 변환하



---

## problem_e

- 알고리즘을 통한 데이터 출력
  - 개봉일이 12월인 영화들의 제목을 리스트로 출력하는 함수 dec_movies

:heart: **1. id_list 만들기 / 2. id_list 영화의 상세정보 불러오기 / 3. release_data에서 12월에 개봉하는 영화 리스트 **

```
import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    
    # release_date
    # movies = [{}, {}, {}]

    
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
```

- 날짜 형태의 값에서 month만 추출하는 방법을 알지 못해서 month에 해당하는 부분만 slicing


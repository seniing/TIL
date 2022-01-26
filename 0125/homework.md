#### 1. Built-in 함수와 메서드

- **sorted()**와 **.sort()**의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

  ```
  import random
  lotto = random.sample(range(1, 46), 6)
  print(lotto) #=> [30, 10, 20, 14, 23, 19]
  ```

  ```
  # sorted() : 새로운 정렬된 리스트로 만들어서 반환
  print(sorted(lotto)) #=> [2, 16, 24, 31, 33, 44]
  ```

  ```
  # .sort() : 원본 list를 정렬해서 변환
  print(lotto.sort()) #=> None
  print(lotto) #=> [2, 16, 24, 31, 33, 44]
  ```

  

#### 2. .extend()와 .append()

- **.extend()**와 **.append()**의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

  ```
  cafe = ['starbucks', 'tomntoms', 'hollys']
  print(cafe) #=>['starbucks', 'tomntoms', 'hollys']
  ```

  ```
  # .append(x) : list끝에 x를 추가
  cafe.append('banapresso')
  print(cafe) #=> ['starbucks', 'tomntoms', 'hollys', 'banapresso']
  
  cafe.append(['coffenie'])
  print(cafe) #=> ['starbucks', 'tomntoms', 'hollys', 'banapresso', ['coffenie']]
  ```

  ```
  # .extend(iterable) : 리스트 끝에 iterable의 모든 항목 추가
  cafe.extend(['wcage', '빽다방'])
  print(cafe) #=> ['starbucks', 'tomntoms', 'hollys', 'wcage', '빽다방']
  
  cafe.extend(['twosome_place'])
  print(cafe) #=> ['starbucks', 'tomntoms', 'hollys', 'wcage', '빽다방', 'twosome_place']
  
  cafe.extend('ediya')
  print(cafe)
  #=> ['starbucks', 'tomntoms', 'hollys', 'wcage', '빽다방', 'twosome_place', 'e', 'd', 'i', 'y', 'a'] 
  ```

  

#### 3. 복사가 잘 된 건가?

- 아래의 코드를 실행 하였을 때, 변수 a와 b에 담긴 list의 요소가 같은지 혹은 다른지 여부를 판단하고 그 이유를 작성하시오.

  ```
  a = [1, 2, 3, 4, 5]
  b = a
  
  a[2] = 5
  
  print(a) #=> [1, 2, 5, 4, 5]
  print(b) #=> [1, 2, 5, 4, 5]
  ```

  ```
  list의 요소가 같다.
  b에 a를 할당하기 때문에 b도 함께 바뀐다.
  b와 a는 같은 list
  ```
  
  


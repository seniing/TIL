#### 1. 모음은 몇 개나 있을까?

- 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 **count_vowels** 함수를 작성하시오. 단, .count() 메서드를 활용하여 작성하시오.

  ```
  count_vowels('apple') #=> 2
  count_vowels('banana') #=> 3
  ```

  ```
  def count_vowels(word):
      word_count = 0
      my_list = ['a', 'e', 'i', 'o', 'u']
      for i in my_list:
          word_count += word.count(i)
      return word_count
  ```

  



#### 2. 문자열 조작

- 다음 중, 문자열(string)을 조작하는 방법으로 옳지 않은 것을 고르시오.

  ```
  (1) .find(x)는 x의 첫번째 위치를 반환한다. 없으면 -1을 반환한다.
  (2) .split([chars])은 특정 문자를 지정하면 문자열을 특정 문자를 기준으로 나누어 list로 변환한다. 특정 문자를 지정하지 않으면 공백을 기준으로 나눈다.
  (3) .replace(old, new[, count])는 바꿀 대상 문자를 새로운 문자로 바꿔서 반환한다.
  (4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를 찾아 제거한다. 특정 문자를 지정하지 않으면 오류가 발생한다.
  ```

  ```
  (4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를 찾아 제거한다. 특정 문자를 지정하지 않으면 오류가 발생한다. => 특정 문자를 지정하지 않으면 공백을 제거
  ```

  

#### 3. 정사각형만 만들기

- 각각 너비와 높이의 값으로 이루어진 2개의 list를 전달 받아, 각각의 값들을 조합하여 만들 수 있는 정사각형만의 넓이를 담은 list를 반환하는 **only_square_area** 함수를 작성하시오.

  ```
  only_square_area([32, 55, 63], [13, 32, 40, 55])
  #=> [1024, 3025]
  ```

  ```
  def only_square_area(list_1, list_2):
      square_area = []
      for i in list_1:
          for j in list_2:
              if i == j:
                  square_area.append(i * j)
      return square_area
  ```

  
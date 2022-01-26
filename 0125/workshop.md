#### 1. 무엇이 중복일까

- 문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는 **duplicated_letters** 함수를 작성하시오.

  ```
  duplicated_letters('apple') #=> ['p']
  duplicated_letters('banana') #=> ['a', 'n']
  ```

  ```
  def duplicated_letters(word):
      result = []
      for i in set(word):
          if word.count(i) > 1:
              result.append(i)
      return result
  
  print(duplicated_letters('apple')) #=> ['p']
  print(duplicated_letters('banana')) #=> ['a', 'n']
  ```

  

#### 2. 소대소대

- 문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여 반환하는 **low_and_up** 함수를 작성하시오. 이때, 전달 받는 문자열은 알파벳으로만 구성된다.

  ```
  low_and_up('apple') #=> aPpLe
  low_and_up('banana') #=> bAnAnA
  ```

  ```
  def low_and_up(word):
      new_word = ''
      for i in range(len(word)):
          if i % 2:
              new_word += word[i].upper()
          else:
              new_word += word[i].lower()
      return new_word
  
  print(low_and_up('apple')) #=> aPpLe
  print(low_and_up('banana')) #=> bAnAnA
  ```
  
  

#### 3. 솔로 천국 만들기

- 정수 0부터 9까ㅏ지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남기고 제거한 list를 반환하는 **lonely** 함수를 작성하시오. 이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다.

  ```
  lonely([1, 1, 3, 3, 0, 1, 1]) #=> [1, 3, 0, 1]
  lonely([4, 4, 4, 3, 3]) #=> [4, 3]
  ```

  ```
  def lonely(lst):
      new_lst = []
      for i in range(len(lst)):
          if i == 0:
              new_lst.append(lst[i])
          elif lst[i] == lst[i-1]:
              pass
          else:
              new_lst.append(lst[i])
      return new_lst
  
  print(lonely([1, 1, 3, 3, 0, 1, 1])) #=> [1, 3, 0, 1]
  print(lonely([4, 4, 4, 3, 3])) #=> [4, 3]
  ```

  

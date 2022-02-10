#### 1. Type Class

- Python은 객체 지향 프로그래밍 언어이다. Python에서 기본적으로 정의되어 있는 클래스를 최소 5가지 이상 작성하시오.

  ```
  int, str, dict, list, set
  ```

  

#### 2. Magic Method

- 아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.

  ```
  __init__, __del__, __str__, __repr__
  ```

  ```
  1. __init__ : 인스턴스 객체가 생성될 때 자동으로 호출되는 함수
  2. __del__ : 인스턴스 객체가 소멸(파괴)되기 직전에 자동으로 호출되는 함수
  3. __str__ : 특정 객체를 출력(print()) 할 때 보여줄 내용을 정의
  4. __repr__ : 정보전달
  ```
  
  

#### 3. Instance Method

- .sort()와 같이 문자열, 리스트, 딕셔너리 등을 조작 할 때 사용하였던 것들은 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드를 최소 3가지 이상 그 역할과 함께 작성하시오.

  ```
  - 문자열 메서드 : find, index, strip, split, replace, upper/lower
  - 리스트 메서드 : append, extend, count, pop, remove
  - 딕셔너리 메서드 : keys, values, items, get
  ```




#### 4. Module Import

```
# fibo.py

def fibo_recursuon(n):
	if n < 2:
		return n
	else:
		return fibo_recursion(n-1) + fibo_recursion(n-2)
```

위와 같은 코드가 같은 폴더 안의 fibo.py 파일에 작성되어 있을 때, 아래와 같은 형태로 함수를 실행 할 수 있도록 하는 import 문을 빈칸 **(a), (b), (c)**를 채워 넣어 완성하시오.

```
from (a)fibo import (b)fibo_recursion as (c)recursion

recursion(4)
```


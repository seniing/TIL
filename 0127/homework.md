#### 1. Circle 인스턴스 만들기

- 아래와 같은 Circle 클래스가 있을 때, 반지름이 3이고 x,y좌표가 (2, 4)인 Circle 인스턴스를 만들어 넓이와 둘레를 출력하시오.

  ```
  class Circle:
      pi = 3.14
  
      def __init__(self, r, x, y):
          self.r = r
          self.x = x
          self.y = y
  
      def area(self):
          return Circle.pi * self.r * self.r
  
      def circumference(self):
          return 2 * Circle.pi * self.r
  
      def center(self):
          return (self.x, self.y)
  ```

  ```
  c1 = Circle(3, 2, 4)
  c1.area()
  c1.circumference()
  
  print(c1.area()) # => 28.26
  print(c1.circumference()) # => 18.84
  ```



#### 2. Dog과 Bird는 Animal이다

- 다음과 같이 Animal 클래스가 주어질 때, 해당 클래스를 상속 받아 아래의 보기와 같이 동작하는 Dog 클래스와 Bird 클래스를 작성하시오.

  ```
  class Animal:
      def __init__(self, name):
          self.name = name
  
      def walk(self):
          print(f'{self.name}! 걷는다!')
      
      def eat(self):
          print(f'{self.name}! 먹는다!')
  ```

  ```
  class Dog(Animal):
      def __init__(self, name):
          super().__init__(name)
  
      def walk(self):
          print(f'{self.name}! 달린다!')
  
      def bark(self):
          print(f'{self.name}! 짖는다!')
  
  class Bird(Animal):
      def __init__(self, name):
          super().__init__(name)
      
      def fly(self):
          print(f'{self.name}! 푸드덕!')
  ```

  ```
  dog = Dog('멍멍이')
  dog.walk() # 멍멍이! 달린다!
  dog.bark() # 멍멍이! 짖는다!
  
  bird = Bird('구구')
  bird.walk() # 구구! 걷는다!
  bird.eat() # 구구! 먹는다!
  bird.fly() # 구구! 푸드덕!
  ```

  

#### 3. 오류의 종류

- 아래에 제시된 오류들이 각각 어떠한 경우에 발생하는지 간단하게 작성하시오.

  ```
  ZeroDivisionError, NameError, TypeError, IndexError, KeyError, ModuleNotFoundError, ImportError
  ```

  ```
  ZeroDivisionError : 어떤 수를 0으로 나누게 될 경우
  NameError : 어느 곳에서도 정의되지 않은 변수를 호출하였을 경우
  TypeError : 자료형이 올바르지 못한 경우
  			함수 호출 과정에서 필수 매개변수가 누락된 경우 혹은 매개변수 개수가 초과해서 들어온 경우
  IndexError : 존재하지 않는 index로 조회할 경우
  KeyError : 존재하지 않는 Key로 접근한 경우
  ModuleNotFoundError : 존재하지 않는 Module을 import 하는 경우
  ImportError : Module은 찾았으나 존재하지 않는 클래스/함수를 가져오는 경우
  ```

  
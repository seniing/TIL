#### 1. CSS flex-direction

- Flex box의 주축을 변경하는 flex-direction의 4가지 값과 각각의 특징을 작성하시오.

```
1. row : inline 방향 [교차축 : 열 방향], 왼쪽에서 오른쪽
2. row-reverse : inline 방향 [교차축 : 열 방향], 오른쪽에서 왼쪽
3. column : block 방향 [교차축 : 행 방향], 위쪽에서 아래쪽
4. colunm-reverse : block 방향 [교차축 : 행 방향], 아래쪽에서 위쪽
```



#### 2. Bootstrap flex-direction

- flex-direction의 4가지 요소와 대응하는 bootstrap 클래스를 작성하시오.

```
<div class="d-flex flex-row"></div>
<div class="d-flex flex-row-reverse"></div>
<div class="d-flex flex-cloumn"></div>
<div class="d-flex flex-cloumn-reverse"></div>
```



#### 3. align-items

- align-items 속성의 4가지 값과 각각의 특징을 작성하시오.

```
1. stretch : 플렉스 요소의 컨테이너의 높이와 같게 변경된 뒤 연이어 배치
2. flex-start : 플렉스 요소가 플렉스 컨테이너의 위쪽에 배치
3. flex-end : 플렉스 요소가 플렉스 컨테이너의 아래쪽에 배치
4. center : 플렉스 요소가 플레스 컨테이너의 가운데에 배치
5. baseline : 플렉스 요소가 플렉스 컨테이너의 기분선(baseline)에 배치
```





#### 4. flex-flow

- flex-flow 속성은 두가지 속성의 축약형이다. 올바르게 짝지어진 것을 고르시오. 

```
(1) flex-direction, flex-wrap 
(2) flex-direction, align-items 
(3) justify-content, flex-wrap 
(4) justify-content, align-item
```

```
(1) flex-direction, flex-wrap 
```



#### 5. Bootstrap Grid System

- 하단 코드에 Bootstrap Grid System을 적용시키고자 할 때, `__(a)__`, `__(b)__` 각각에 입력해야 할 클래스 이름을 작성하시오.

```
<div class="__(a)__">
	<div class="__(b)__"
		<div class="col-__(c)__-__(d)__"></div>
	</div>
</div>
```

```
__(a)__ : container, __(b)__ : row
```





#### 6. Breakpoint prefix

- Bootstrap Grid System에서 요소의 크기를 지정하기 위해서는 상단 코드와 같은 형태로 클래스 이름을 지정해야 한다.

  1. `__(c)__`에 들어갈 수 있는 값과 그 값들이 가지는 의미를 작성하시오. 

  | Breakpoin         | Class infix | Dimensins  |
  | ----------------- | ----------- | ---------- |
  | X-Small           | `None`      | < 576 px   |
  | Small             | `sm`        | >= 576 px  |
  | Medium            | `md`        | >= 768 px  |
  | Large             | `lg`        | >= 992 px  |
  | Extra latge       | `xl`        | >= 1200 px |
  | Extra extra large | `xxl`       | >= 1400 px |

  

  2. `__(d)__`에 들어갈 수 있는 값과 그 값들이 가지는 의미를 작성하시오

```
1 부터 12 까지의 숫자가 들어갈 수 있다. columns의 크기가 12.

<div class="col col-lg-2"></div> -> lg(992)이상일 때 2칸을 차지

<div class="row">
      <div class="col-md-8">.col-md-8</div> 
      -> md(768)이상일 때 8칸을 차지
      <div class="col-6 col-md-4">.col-6 .col-md-4</div> 
      -> md(768)이상일 때 4칸을 차지, 미만일 경우 6칸 차지
   </div>
</div>
```


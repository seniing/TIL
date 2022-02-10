#### 1. HTML 정의

- 아래의 보기 (1) ~ (4) 중에서, HTML의 본딧말을 고르시오.

```
(1) Hyperlinks and Text Markup Language
(2) Home Tool Markup Language
(3) Hyper Text Markup Language  #=>HTML
(4) Hyper Tool Markup Language
```

**Hyper Text Markup Language**



#### 2. HTML 개념

- 각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오. 
  1. 웹 표준을 만드는 곳은 Mozilla 재단이다. **(F)**
     - W3C, WHATWG
  2. 표(table)를 만들 때에는 반드시 `<th>` 태그를 사용해야 한다. **(F)**
     - table 태그 기본 구성 : thead(`<tr>` > `<th>`), tbody(`<tr>` >`<td>`), tfoor(`<tr>` >`<td>`), caption
     - `<tr>`은 가로줄을 구성, `<th>`, `<td>`로 내부 셀 구성
  3. 제목(Heading) 태그는 제목 이외에는 사용하지 않는 것이 좋다. **(T)**
  4. 리스트를 나열하기 위해서는 `<ul>` 태그만 사용 할 수 있다. **(F)**
     - `<ol>` / `</ol>` : 순서가 있는 리스트(ordered)
     - `<ul>` / `</ul>` : 순서가 없는 리스트(unordered))
  5. HTML의 태그는 반드시 별도의 닫는 태그가 필요하다. **(F)**



#### 3. CSS 정의

- 아래의 보기 (1) ~ (4) 중에서, CSS의 본딧말을 고르시오.

```
(1) Creative Style Sheets
(2) Cascading Style Sheets #=>CSS
(3) Computer Style Sheets
(4) Colorful Style Sheets
```

**Cascading Style Sheets**



#### 4. CSS 개념

- 각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오.
  1. HTML과 CSS는 각자 문법을 갖는 별개의 언어이다. **(T)**
     - CSS : 스타일을 지정하기 위한 언어
  2. 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다. **(T)**
  3. 자식 요소 프로퍼티는 부모의 프로퍼티를 모두 상속 받는다. **(F)**
     - 상속 되는 것 예시 : Text 관련 요소(font, color, text-align), opacity, visibility 등
     - 상속 되지 않는 것 예시 : Box model 관련 요소(width, height, margin, padding, box-sizing, display), position 관련 요소(position, top/right/bottom/left, z_index) 등
  4. 디바이스마다 화면의 크기가 다른 것을 고려하여 상대 단위인 %를 사용한다. **(F)**
  5. id 값은 유일해야 하므로 중복되어서는 안된다. **(T)**



#### 5. CSS 우선순위

- CSS는 우선 적용되는 순서가 존재 한다. 우선순위가 높은 순으로 나열 하시오.

```
요소 선택자, Inline style, 소스 순서,
!important, id 선택자, class 선택자
```

```
!important > Inline stycle > id 선택자 > class 선택자 > 요소 선택자 > 소스 순서
```


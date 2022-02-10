### Bootstrap Component

- 아래의 페이지를 Bootstrap Component
  1. 각 요소(nav, header, section, footer)는 주어진 코드의 주석에 맞춰 작성합니다. 
  2. 모든 이미지 요소는 주어진 이미지 파일을 활용합니다.
  3. 모든 구성 요소 배치는 flexbox를 활용 합니다.
  4. 모든 텍스트 스타일은 공식 문서의 typography를 참고하여 작성합니다



#### Nav

1. 네비게이션 바는 항상 브라우저 화면 최상단에 고정되어 있습니다.
2. 네비게이션 바의 배경색은 공식 문서의 background color 를 참고하여 작성합니다. 
3. 로고 이미지와 네비게이션 리스트는 각각 네비게이션 바 양 끝에 배치합니다.
4. 리스트의 항목 간 간격은 2rem입니다. 공식 문서의 spacing을 참고하여 작성합니다.
5. 리스트의 각 항목들은 마우스를 올렸을 때, 밑줄이 나오지 않도록 설정합니다.
6. 위에 명시된 내용 이외에는 자유롭게 작성합니다. 

```
  <nav class="d-flex justify-content-between fixed-top bg-dark">
    <a href="#">
      <img src="images/logo.png" alt="Logo Image">
    </a>
    <ul class="d-flex my-auto align-items-center">
      <li class="mx-3"><a href="#" class="text-decoration-none text-light">Home</a></li>
      <li class="mx-3"><a href="#" class="text-decoration-none text-light">Community</a></li>
      <li class="mx-3"><a href="#" class="text-decoration-none text-light">Login</a></li>
    </ul>
  </nav>
```



#### Header

1. Header 내부의 요소(글, 버튼)는 수직, 수평 중앙에 배치 합니다.
2. Header 내부의 글씨 색상은 흰색이며, 굵기는 bold 입니다.
3. Header 내부의 글씨 크기는 공식 문서의 display heading을 활용합니다.
4. Header 내부의 버튼의 색상은 파란색이며 크기는 크게 설정합니다.
5. 위에 명시된 내용 이외에는 자유롭게 작성합니다. 

```
  <header class="d-flex justify-content-center align-items-center text-light">
      <div class="text-center display-1 fw-bold">Cinema</div>
      <div class="text-center display-1 fw-bold">Community</div>
      <a href="#" type="button" class="btn btn-primary btn-lg text-light">Let's Go</a>
  </header>
```



#### Section

1. Section 내부의 요소(글, 이미지)는 수평 중앙에 배치 합니다.
2. Section 내부의 3개의 이미지는 수평으로 나열되어 있습니다.
3. Section 내부의 이미지간 간격은 동일합니다.
4. Section 내부의 이미지 아래에는 이미지를 설명하는 간단한 글이 있습니다.
5. 위에 명시된 내용 이외에는 자유롭게 작성합니다. 

```
  <section>
    <h2>Used Skills</h2>
    <article class="d-flex justify-content-around align-items-center text-center">
      <div>
        <img src="images/web.png" alt="Web Image">
        <p>Web</p>
      </div>
      <div>
        <img src="images/html5.png" alt="HTML5 Image">
        <p>HTML5</p>
      </div>
      <div>
        <img src="images/css3.png" alt="CSS3 Image">
        <p>CSS3</p>
      </div>
    </article>
  </section>
```



#### Footer

1. Footer는 항상 브라우저 화면 최하단에 고정되어 있습니다.
2. Footer의 배경색은 파란색입니다.
3. Footer에 작성된 내용은 수직, 수평 중앙에 배치 합니다.
4. Footer에 작성된 내용의 빈 부분( _____ )은 본인의 이름을 작성해 주세요.
5. 위에 명시된 내용 이외에는 자유롭게 작성합니다. 

```
  <footer class="d-flex justify-content-center align-items-center fixed-bottom bg-primary">
    <p>HTML & CSS project. Created by _____</p>
  </footer>
```



### 최종

```
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <title>Document</title>
</head>
<body>
  <!-- 1. Nav -->
  <nav class="d-flex justify-content-between fixed-top bg-dark">
  <!-- <nav class="d-flex justify-content-between sticky-top bg-dark"> -->
    <a href="#">
      <img src="images/logo.png" alt="Logo Image">
    </a>
    <ul class="d-flex align-items-center mb-0 list-unstyled">
      <li class="mx-3"><a href="#" class="text-decoration-none text-light">Home</a></li>
      <li class="mx-3"><a href="#" class="text-decoration-none text-light">Community</a></li>
      <li class="mx-3"><a href="#" class="text-decoration-none text-light">Login</a></li>
    </ul>
  </nav>

  <!-- 2. Header -->
  <header class="d-flex flex-column justify-content-center align-items-center">
      <div class="text-light fw-bold display-1">Cinema</div>
      <div class="text-light fw-bold display-1">Community</div>
      <a href="#" type="button" class="btn btn-primary btn-lg mt-5">Let's Go</a>
  </header>

  <!-- 3. Section -->
  <section class="d-flex flex-column align-items-center mt-5">
    <h2>Used Skills</h2>
    <article class="d-flex text-center mt-3">
      <div>
        <img src="images/web.png" alt="Web Image">
        <p>Web</p>
      </div>
      <div>
        <img src="images/html5.png" alt="HTML5 Image">
        <p>HTML5</p>
      </div>
      <div>
        <img src="images/css3.png" alt="CSS3 Image">
        <p>CSS3</p>
      </div>
    </article>
  </section>

  <!-- 4. Footer -->
  <footer class="fixed-bottom bg-primary d-flex justify-content-center align-items-center">
    <p class="mb-0 text-light fw-bold">HTML & CSS project. Created by seniing</p>
  </footer>
</body>
</html>
```


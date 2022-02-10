#### 1. img tag

- 아래 그림과 같은 폴더 구조가 있다. resume.html에서 코드를 작성 중일 때, image 폴더 안의 my_photo.png를 보여주는`<img>` tag를 작성하시오. 단, 이미지가 제대로 출력되지 않을 때는 ssafy 문자열이 출력 되도록 작성하시오

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <img src="C:\Users\user\Desktop\ssafy7\image\my_photo.jpg" alt="ssafy">
</body>
</html>
```



#### 2. 파일 경로

- 위와 같이 경로를 `__(a)__`로 작성 할 시, github에 업로드 하거나 전체 폴더의 위치가 변경 되었을 때 이미지를 불러 올 수 없게 된다. 이를 해결 하려면 이미지 경로를 `__(b)__` 로 바꾸어 작성하면 된다.  `__(a)__`와 `__(b)__`에 들어갈 말과 `__(b)__` 로 변경한 코드를 작성하시오.

```
(a) : C:\Users\user\Desktop\ssafy7\image\my_photo.jpg
(b) : ..\image\my_photo.jpg
```

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <img src="..\image\my_photo.jpg" alt="ssafy">
</body>
</html>
```





#### 3. Hyper Link

- 출력된 my_photo.png 이미지를 클릭하면 ssafy.com으로 이동하도록 하시오.

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <a href="https://www.ssafy.com">
    <img src="..\image\my_photo.jpg" alt="ssafy">
  </a>
</body>
</html>
```



#### 4. 선택자

1. 아래의 코드를 작성하고 결과를 확인 하시오.

```
<div id="ssafy">
	<h2>어떻게 선택 될까?</h2>
	<p>첫번째 단락</p>
	<p>두번째 단락</p>
	<p>세번째 단락</p>
	<p>네번째 단락</p>
</div>
```

```
#ssafy > p:nth-child(2) {
	color: red;
}
```

**첫 번째 단락의 색깔이 레드로 바뀐다.**



2. nth-child를 nth-of-type으로 변경하고 결과를 확인 하시오.

```
#ssafy > p:nth-of-type(2) {
	color: blue;
}
```

**두 번째 단락의 색깔이 블루로 바뀐다.**



3. 작성한 코드를 참고하여 nth-child()와 nth-of-type()의 차이점을 작성하시오.
   - nth-chile() : 모든요소를 포함해 순서 카운트
   - nth-of-type() : 특정요소들 안에서만 순서 카운트

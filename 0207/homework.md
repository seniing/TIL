### Bootstrap

- 공식 문서의 Component를 활용하여 물음에 답하시오.
  1. 각 문항에 제시된 이미지는 현재 lab.ssafy.com에서 사용중인 components이다. 제시된 요소에 사용된 Bootstrap Component 를 참고하여 빈칸을 작성하시오.



#### 1. Components

```
<button type="submit" class="                                          ">Sign in</button>
```

```
<button type="submit" class="d-grid gap-2 col-6 mx-auto btn btn-success">Sign in</button>
```



#### 2. Components

```
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <!-- Image and text -->
      <a class="navbar-brand" href="#">
        <img src="#" alt="#" width="30" height="24" class="d-inline-block align-top">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdowm">
        <span class="navbar-toggler-icon"></span>>
      </button>

      <!-- Dropdown & Item -->
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle active" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown">
              프로젝트
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle active" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown">
              그룹들
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="#">활동</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="#">마일스톤</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="#">스티펫</a>
          </li>
        </ul>
      </div>
    </div>
   </nav> 
```

```
a = dark, b = navbarNavDropdown, c = navbar-nav
```



#### 3. Components

```
   <nav aria-label="...">
    <ul class="pagination justify-content-center">
      <li class="page-item disabled">
        <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Prev</a>
      </li>
      <li class="page-item active" aria-current="page">
        <a class="page-link" href="#">1</a>
      <li class="page-item"><a class="page-link" href="#">2</a></li>
      <li class="page-item"><a class="page-link" href="#">3</a></li>
      <li class="page-item"><a class="page-link" href="#">4</a></li>
      <li class="page-item">
        <a class="page-link" href="#">Next</a>
      </li>
    </ul>
  </nav>
```

```
a = pagination justify-content-center, b = disabled, c = active
```


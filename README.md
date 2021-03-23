# Classify your Photos

인공지능 모델을 통해 사진을 분류하여 정렬해주는 웹서비스 

사용자가 로그인 하여 사진을 업로드 할 수 있다.

사진이 정상적으로 업로드 되면 모듈에서 사진을 분류해 태그값이 발생한다.

분류 된 사진은 업로드한 사용자 본인만 볼 수 있도록 구현했다.

사진은 태그 순, 최신 업로드 순 으로 확인 가능하다.

# 개발 환경

WEB - Django Framework (python) 
Inception v3 모델 사용
DB - sqlite 사용

# 개발 동기
사진의 양이 많아져 구분하기 어려울 때 분류 해주는 서비스의 구현

# 구현
로그인의 구현은 django.contrib.auth와 models로 제공되는 User 모델을 통해 구현했다.
사진 업로드시 @login_required 데코레이터 작성으로 토큰을 확인해 로그인 한 사용자만 업로드 할 수 있도록 구현했다.
분류 태그는 Inception v3 모델을 태그별로 100장을 넣은 폴더에서 500번 재학습 (Retraining) 시켜 분류하도록 구현했다.


# 프레임워크 장단점
1. Python 기반으로 간단하고 직관적인 결과물을 기대할수 있다.
2. 로그인, 인증 등의 반복 사용되는 데이터의 라이브러리가 많이 구현되어있다.

# 라이브러리 구조 공부
1. MTV 패턴 
Django Views는 MVC 패턴의 Controller과 비슷한 역할을 한다.
views.py 라는 파일에 정의된 하나의 함수가 각 하나의 View를 정의한다.
각 View는 HTTP Request를 입력 파라미터로 받아들이고, HTTP Response를 리턴한다.

Django Template은 MVC 패턴의 View와 비슷한 역할을 한다. 
Template은 "templates"이라는 서브폴더 안에 HTML 파일을 두어 생성한다.
Template는 View로부터 전달된 데이터를 템플릿에 적용하여 동적인 웹페이지를 만드는데 사용된다.

Django Model은  models.py 모듈 안에 정의하게 된다.
models.py 모듈은 데이터베이스의 한 테이블에 해당하며 안에 여러개의 모델 클래스를 정의 할 수 있다.

2. DTL(Django Template Language) : Django 템플릿 언어
Template 생성시 변수와 논리 제어 태그를 일부 DTL로 구현한다. 

# 프로젝트 소개

- 쇼핑몰 일부 만들기

- 회원 관리
- 상품 관리
- 주문 관리

## 클래스를 활용한 뷰 생성

- 함수 VS 클래스 => 뷰의 재사용
- 데코레이터 => 기능의 재사용

## DRF로 RESTful API도 개발

- 상품등록은 관리자 계정만
- 어떤 view는 관리자만, 


# setting

## fc_shp
- virtualenv fc_env
- source fc_env/bin/activate
- pip install django

## fc_shp/fc_django

- django-admin startapp fcuser
- django-admin startapp product
- django-admin startapp order

# create Model

# class based view

- class가 재사용성이 더 좋음

```
class 기반의 generic view
코드의 반복을 줄이기 위해 함수,클래스
함수를 만들면 상속이 생김

```

```python
# ex)
from django.views.generics import ListView
from books.models import Publisher

class PublisherList(ListView):
    model = Publisher

```

## 상품목록조회

```
<!-- {% for product in object_list %} -->
<!-- {% for product in product_list %}
{{product.name}}:{{product.price}}
{% endfor %} -->

```

### django

```
Built-in tag reference
```
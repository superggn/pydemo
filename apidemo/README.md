# README

##### 概述

django openapi3 最小实现

使用 DRF (Django REST Framework) + drf-spectacular 实现 openapi3 版本的 API 文档

##### 启项目

```
django-admin startproject apiDemo
python manage.py startapp demo
```

不用改 db settings， 默认的 sqlite 就能用

```
pip install Django
pip install djangorestframework
pip install drf-spectacular
```

##### workflow

- urls.py
    - 在 url 里带上 SpectacularAPIView 来生成 api schema
    - 使用 SpectacularRedocView / SpectacularSwaggerView 来将 api schema 渲染为前端， 进行交互
- views.py
    - 在每个需要生成文档的 api view 之前加上 @extend_schema 这个装饰器即可生成 api doc

- 跑一下即可在浏览器看到 api doc
    - > python3 manage.py runserver
    - http://127.0.0.1:8000/api/docs/


##### 背景知识

openapi（之前的 swagger） 是 api 接口的事实标准， DRF 内置的 api schema 实现已停止维护， drf 内置实现的正统续作是
drf-spectacular

##### 碰到的问题

- response 的 example 能加载出来， 但 request 的例子加载不出来
    - 这是因为 request 必须要指定 serializer 才能加载出来例子
    - 换句话说， 如果 extend_schema 的 request 参数不指定为 serializer, 就没法在 api doc 中写例子


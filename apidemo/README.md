# README

##### 概述

django openapi3 最小实现

使用 DRF (Django REST Framework) + drf-spectacular 实现 openapi3 版本的 API 文档

##### 启项目

```
django-admin startproject apiDemo
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

##### 背景知识

openapi（之前的 swagger） 是 api 接口的事实标准， DRF 内置的 api schema 实现已停止维护， drf 内置实现的正统续作是
drf-spectacular




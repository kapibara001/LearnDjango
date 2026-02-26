from django.urls import path, re_path, include
from  hello import views


product_patterns = [
    path("", views.products),
    path("comments", views.comments),
    path("questions", views.questions),
]

urlpatterns = [
    re_path(r'^about/contact', views.contact),

    # Работа с параметрами маршрута 
    # path("user", views.user),
    # path("user/<str:name", views.user),
    # path("user/<str:name>/<int:age>", views.user), 

    # Параметры маршрута через re_path
    ## В отличие от метода с path теперь более конкретные маршруты размещаются выше
    # re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
    # re_path(r"^user/(?P<name>\D+)", views.user),
    # re_path(r"^user", views.user),

    re_path(r'^about', views.about, kwargs={"name": "Tom", "age": 22}),

    path('index', views.index), # begin only with /
    re_path(r'^secCode', views.HttpresponseDemostration),
    # path('home/m', views.homepage, name="Fun"),

    # Использование include для подмаршрутов
    path("products/<int:id>/", include(product_patterns)),

    # Работа не с параметрами маршрута user/Tim/15, а с параметрами строки запроса ?name=Tim&age=15
    path("user/", views.user),

    # Редиррект функция
    path("123", views.redirectFunc),

    path("peoples/<int:id>", views.index2),
    # path("access/<int:age>", views.access),
    path("access/", views.access)
]

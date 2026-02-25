"""
URL configuration for LDP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from  hello import views

urlpatterns = [
    re_path(r'^about/contact', views.contact),

    # Работа с параметрами маршрута 
    # path("user", views.user),
    # path("user/<str:name", views.user),
    # path("user/<str:name>/<int:age>", views.user), 

    # Параметры маршрута через re_path
    ## В отличие от метода с path теперь более конкретные маршруты размещаются выше
    re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
    re_path(r"^user/(?P<name>\D+)", views.user),
    re_path(r"^user", views.user),

    re_path(r'^about', views.about, kwargs={"name": "Tom", "age": 22}),

    path('index', views.index), # begin only with /
    re_path(r'^secCode', views.HttpresponseDemostration),
    # path('home/m', views.homepage, name="Fun"),
]

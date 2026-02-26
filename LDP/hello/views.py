from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden

# We can send html-code in Response

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path

    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>User agent: {user_agent}</p>
        <p>Path: {path}</p> 
        """) # Send string to user

def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе:</h2>
            <h3>Имя: {name}</h3>
            <h3>Возраст: {age}</h3>
            <h4>{request.get_full_path()}</h4>
        """)

def contact(requst):
    return HttpResponse("<h1>Контакты</h1>")


def HttpresponseDemostration(request):
    ## Возвращение каких-то данных
    # return HttpResponse(
    #     "Hello from HttpresponseDemostration",
    #     headers = {
    #         "Secret_Code": "2102102519",
    #     }
    # )

    ## Возвращение ошибки
    # return HttpResponse(
    #     "Произошла ошибка",
    #     status = 400,
    #     reason = "Incorrect data",
    # )

    ## Пример возвращения данных с другими заголовками
    return HttpResponse(
        "<h1>Hello</h1>",
        content_type="text/plain", # Теги отображаются на странице, несмотря на их правильность
        charset="utf-8",
    )

# Параметры маршрута
# Если мы не укажем параметры в маршруте - будет ошибка 404. Чтобы избежать, можно поставить параметры по умолчанию
# def user(request, name, age):
# def user(request, name="Undefined", age=0):
#     if name.lower() in ['hack']:
#         return HttpResponse(
#             "<h2>Bad response</h2>",
#             status = 333,
#             reason = "Unknown data",
#         )

#     return HttpResponse(
#         f"<h2>Имя: {name}, возраст: {age}</h2>"
#     )


def products(request, id):
    return HttpResponse(f"Продукт {id}")

def comments(request, id):
    return HttpResponse(f"Комментарии про продукт {id}")

def questions(request, id):
    return HttpResponse(f"Вопросы про продукт {id}")


def user(request:HttpResponse):
    # Для получения параметра строки запроса применяется req.GET.get('имя параметра')
    # name = request.GET.get('name')
    # age = request.GET.get('age')

    # Если не переданы аргументы /user/ - будут применяться аргументы по умолчанию
    name = request.GET.get("name", "Undefined")
    age = request.GET.get("age", 0)

    return HttpResponse(f"""
        <h1>Информация: </h1>
        <h1>{name}</h1>
        <h2>{age}</h2>
    """)


# Редирект функция
def redirectFunc(request):
    return HttpResponseRedirect('/about')

# 
def index2(request, id):
    peoples = ["Maxim", "Bob", "Daniil", "Alexander"]

    if id in range(len(peoples)):
        return HttpResponse(f"""
            <h1>{peoples[id]}</h1>
        """)
    else:
        return HttpResponseNotFound("Error: Not found")
    
def access(request, age=0):
    age = request.GET.get('age')
    age = int(age)

    if age not in range(1, 111):
        return HttpResponseBadRequest("Неверный возраст")
    else:
        if age > 17:
            return HttpResponse("Доступ разрешен")
        else:
            return HttpResponseForbidden("Доступ запрещен: недостаточно лет")
        
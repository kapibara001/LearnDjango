from django.http import HttpResponse

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
def user(request, name="Undefined", age=0):
    if name.lower() in ['hack']:
        return HttpResponse(
            "<h2>Bad response</h2>",
            status = 333,
            reason = "Unknown data",
        )

    return HttpResponse(
        f"<h2>Имя: {name}, возраст: {age}</h2>"
    )
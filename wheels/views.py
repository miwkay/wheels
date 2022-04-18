from django.http import HttpResponse
# from django.shortcuts import render


# from Django.Wheels.wheels.models import Rubber, Discs


def index(request):
    return HttpResponse("<h3>Перейдите в раздел <h2>/wheels</h2></h3>")


# def wheels(request):
#     return render(request, 'wheels.html')

def wheels(request):
    return HttpResponse("<h1>Успех!</h1>")

# def wheels(request):
#     amount_rubber = Rubber.objects.count()
#     amount_discs = Discs.objects.count()
#     return HttpResponse(f"<h3>Всего автомобильной резины: {amount_rubber}"
#                         f"Всего автомобильных дисков: {amount_discs}</h3>")

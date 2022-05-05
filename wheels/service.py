from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Операция выполнена успешно.',
        'bestoilmotul@gmail.com',
        [user_email],
        fail_silently=False,
    )

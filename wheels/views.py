from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import CreateView

from rest_framework import generics

from .forms.WheelsForm import ContactForm
from .models import Contact, Disc, Rubber
from .serializers import DiscSerializer, RubberSerializer
from .tasks import send_spam_email


class DiscAPIView(generics.ListAPIView):
    queryset = Disc.objects.all()
    serializer_class = DiscSerializer


class RubberAPIView(generics.ListAPIView):
    queryset = (
        Rubber.objects
            .filter(brand='Michelin')
            .select_related('brand', 'width', 'profile', 'diametr')
            .values('brand', 'width', 'profile', 'diametr')
    )
    serializer_class = RubberSerializer


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = 'contact/'
    template_name = 'wheels/contact.html'

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)


def index(request):
    return render(request, 'wheels/index.html')


def rubber(request):
    rubber = Rubber.objects.filter(diametr='17')
    return render(request, 'wheels/rubber.html', {'rubber': rubber})


def disc(request):
    discs = Disc.objects.order_by('diametr')
    page_number = request.GET.get('page')
    all_disc = Paginator(discs, 3)
    try:
        discs_all = all_disc.page_number(page_number)
    except PageNotAnInteger:
        discs_all = all_disc.page_number(1)
    except EmptyPage:
        discs_all = all_disc.page_number(all_disc.num_pages)

    return render(request, 'wheels/disc.html', {'discs_all ': discs_all})

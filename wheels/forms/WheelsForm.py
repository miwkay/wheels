from django import forms

from ..models import Contact, Disc, Rubber


class DiscForm(forms.ModelForm):
    class Meta:
        model = Disc
        fields = (
            'brand',
            'diametr',
            'color',
        )


class RubberForm(forms.ModelForm):
    class Meta:
        model = Rubber
        fields = (
            'brand',
            'diametr',
            'season',
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

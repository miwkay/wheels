from Django.Wheels.wheels.models import Disc, Rubber

from django import forms


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

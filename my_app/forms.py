from .models import Car
from django import forms

class CarsCreate(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__' #[title , description]
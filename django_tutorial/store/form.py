from django import forms

from .models import new_user



class new_use(forms.ModelForm):
    class Meta:
        model = new_user
        fields ='__all__'
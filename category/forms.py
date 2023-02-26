from django.db import models
from django.forms import fields
from .models import CustomUpload
from django import forms


class CustomUploadForm(forms.ModelForm):
    caption = forms.CharField(max_length=200)

    class Meta:
        model = CustomUpload
        fields = "__all__"
        widgets = {
            "size" : forms.RadioSelect()
        }

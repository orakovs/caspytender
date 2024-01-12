from django import forms
from .models import *

# Создание новости
class NewsCreationForms(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'category', 'content', 'image']
        widgets = {'image': forms.FileInput(attrs={'multiple': False})}


# Редактирование новости
class NewsChangeForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'category', 'content', 'image']
        widgets = {'image': forms.FileInput(attrs={'multiple': False})}
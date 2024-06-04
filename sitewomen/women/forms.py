from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Husband, Women


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else "Должны присутствовать только русские символы, дефис и пробел."

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", label="Категория:")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label="Не замужем", required=False, label="Муж:")

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'cat', 'husband', 'tags', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'add-page__title', 'placeholder': ' '}),
            'slug': forms.TextInput(attrs={'class': 'add-page__url', 'placeholder': ' '}),
            'content': forms.Textarea(attrs={'class': 'add-page__description', 'cols': 50, 'rows': 5, 'placeholder': ' '}),
            'cat': forms.Select(attrs={'class': 'add-page__select'}),
            'husband': forms.Select(attrs={'class': 'add-page__select'}),
            'tags': forms.SelectMultiple(attrs={'class': 'add-page__select'}),
            'is_published': forms.Select(attrs={'class': 'add-page__select'}),
        }
        # labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Длина превышает 50 символов")

        return title


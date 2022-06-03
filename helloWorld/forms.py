from django import forms
from helloWorld.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("user",)

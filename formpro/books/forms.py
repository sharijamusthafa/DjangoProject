from django import forms
from books.models import Book
from django.forms import ModelForm
# class BookCreateForm(forms.Form):

    # book_name=forms.CharField(max_length=120)
    # author=forms.CharField(max_length=120)
    # price=forms.IntegerField()
    # pages=forms.IntegerField()

class BookCreateForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"

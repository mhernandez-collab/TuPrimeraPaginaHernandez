from django import forms
from .models import Author, Category, Post

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class SearchForm(forms.Form):
    search = forms.CharField(label="Buscar título de post")

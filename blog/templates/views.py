from django.shortcuts import render, redirect
from .forms import AuthorForm, CategoryForm, PostForm, SearchForm
from .models import Post

def home(request):
    return render(request, 'home.html')

def create_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create_author.html', {'form': form})

def create_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create_category.html', {'form': form})

def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create_post.html', {'form': form})

def search_post(request):
    results = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['search']
            results = Post.objects.filter(title__icontains=query)
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form, 'results': results})

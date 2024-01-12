from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from .forms import *


def homeView(request):
    news = News.objects.all().order_by('-pub_date')
    paginator = Paginator(news, 4)
    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)
    
    context = {
        'news_page': news_page
    }
    
    return render(request, 'home.html', context)


def newsCreateViews(request):
    if request.method == 'POST':
        form = NewsCreationForms(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.pub_date = timezone.now()
            news.save()
            return redirect('home_url')
    else:
        form = NewsCreationForms()
    return render(request, 'create_news.html', {'form': form})
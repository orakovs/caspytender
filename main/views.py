from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from .forms import *

def homeView(request, category_id=None):
    # Получаем все категории
    categories = NewsCategory.objects.all()

    # Инициализируем переменные
    selected_category = None
    news = News.objects.all().order_by('-pub_date')

    # Если выбрана категория, фильтруем новости
    if category_id:
        selected_category = get_object_or_404(NewsCategory, pk=category_id)
        news = news.filter(category=selected_category)

    paginator = Paginator(news, 4)
    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)

    context = {
        'news_page': news_page,
        'selected_category': selected_category,
        'categories': categories
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
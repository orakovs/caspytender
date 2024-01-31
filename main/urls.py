from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', homeView, name='home_url'),
    path('add/', newsCreateViews, name='create_news_url'),
    path('<int:category_id>/', homeView, name='home_with_category_url'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.db import models
from django.utils import timezone

# Категория новостей
class NewsCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name='Категория новостей')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name
    

# Новость
class News(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название новости')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, verbose_name='Категория')
    content = models.TextField(verbose_name='Текст новости')
    image = models.ImageField(upload_to='image/news', default='image/news/news_default.jpg', verbose_name='Изображение')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='Дата и время публикации')
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    
    def __str__(self):
        return self.title
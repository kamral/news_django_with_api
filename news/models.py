from django.db import models

# Create your models here.

class News(models.Model):
    title=models.CharField(max_length=100, verbose_name='Название')
    content=models.TextField(blank=True,verbose_name='Контент')
    created_at=models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата создания')
    update_at=models.DateTimeField(auto_now=True,
                                   verbose_name='Время обновления')
    is_published=models.BooleanField(default=True)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
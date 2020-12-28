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
    category=models.ForeignKey('Category',on_delete=models.CASCADE)



    def __str__(self):
        return self.title


    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
        ordering=['-created_at']


class Category(models.Model):
    title=models.CharField(max_length=100,verbose_name='Наименование',db_index=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Category'

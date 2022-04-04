from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название товара")
    description = models.TextField(blank=True,verbose_name="Описание")
    price = models.FloatField(default=0,verbose_name='Цена')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True,verbose_name="Время изменения")
    is_published = models.BooleanField(default=True,verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,verbose_name="Категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-time_create', 'name']

class Category(models.Model):
    name_cat = models.CharField(max_length=100, db_index=True,verbose_name="Категория")


    def __str__(self):
        return self.name_cat

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']



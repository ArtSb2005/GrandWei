from django.db import models

class IndexProduct(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    price = models.CharField(max_length=255, verbose_name='Стоимость')
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ножи собственного производства'
        verbose_name_plural = 'Ножи собственного производства'

class IndexProductImage(models.Model):
    post = models.ForeignKey(IndexProduct, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title






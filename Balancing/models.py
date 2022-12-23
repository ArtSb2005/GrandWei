from django.db import models

# Create your models here.
class BalancingProduct(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    price = models.CharField(max_length=255, verbose_name='Стоимость')
    images = models.FileField(upload_to='images/')
    video = models.FileField(upload_to='images/', blank=True, null=True, verbose_name='Видео(необязательно)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Балансировка и ремонт барабанов'
        verbose_name_plural = 'Балансировка и ремонт барабанов'

class BalancingProductImage(models.Model):
    post = models.ForeignKey(BalancingProduct, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title
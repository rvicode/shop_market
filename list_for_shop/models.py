from django.db import models
from django.urls import reverse


class ListShop(models.Model):
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=5)
    unit = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/shop')

    def get_absolut_url(self):
        return reverse('list_for_shop:detail_shop', kwargs={'pk': self.id})

    def __str__(self):
        return self.title

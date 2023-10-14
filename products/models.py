from django.db import models


# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class product_all(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='product_picture/')
    old_price = models.PositiveIntegerField()
    new_price = models.PositiveIntegerField()
    rate = models.PositiveIntegerField()
    description = models.TextField(max_length=250)
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

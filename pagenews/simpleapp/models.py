from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime

class P(models.Model):
    title_p = models.CharField(max_length=64, unique=True, )
    description_p = models.TextField()
    text_p = models.TextField()
    quantity_p = models.IntegerField(validators=[MinValueValidator(0)], )
    cost_p = models.FloatField(validators=[MinValueValidator(0.0),])
    category_p = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='product', )
    datetime_p = models.DateTimeField(auto_now_add=True, )


    def __str__(self):
        return f'{self.title_p.title()}: {self.description_p[:64]}: {self.text_p}'

class Category(models.Model):
    title_category = models.CharField(max_length=64, unique=True, )

    def __str__(self):
        return self.title_category.title()


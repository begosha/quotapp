from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

class Quote(models.Model):
    text = models.TextField(
        max_length=1200,
        null=False,
        blank=False,
        verbose_name='Text'
    )
    author = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Author'
    )
    email = models.EmailField(null=False, blank=False, verbose_name='Email')
    rating = models.IntegerField(
        null=True,
        blank=True,
        validators=(MinValueValidator(0),),
        verbose_name='Rating'
    )
    status = models.BooleanField(default=False, verbose_name='Moderated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'quotes'
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'

    def __str__(self):
        return f'{self.id}. {self.author}: {self.text}'
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name of category')

    def __str__(self):
        return self.name


class Tag(models.Model):
    RED_COLOR = 'RED'
    BLUE_COLOR = 'BLUE'
    GREEN_COLOR = 'GREEN'
    GRAY_COLOR = 'GRAY'

    COLOR_CHOICES = (
        (RED_COLOR, 'Black'),
        (BLUE_COLOR, 'Blue'),
        (GREEN_COLOR, 'Green'),
        (GRAY_COLOR, 'Gray')
    )

    name = models.CharField(max_length=100, verbose_name='Name of tag')
    color = models.CharField(max_length=16, choices=COLOR_CHOICES, default=GRAY_COLOR,
                              verbose_name='Color of tag')
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name of product')
    description = models.TextField(null=True, blank=True, verbose_name='Description of product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category of product')
    tags = models.ManyToManyField(Tag, verbose_name='Tags of product')

    def __str__(self):
        return self.name


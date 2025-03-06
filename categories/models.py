from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
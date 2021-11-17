from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=156)
    slug = models.SlugField(max_length=156, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.TextField()
    tegs = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    age_date = models.IntegerField()
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=256)
    comment = models.TextField(blank=False)

    def __str__(self):
        return self.first_name

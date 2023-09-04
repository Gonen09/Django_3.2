from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.


class Article(models.Model):
    # Django model-field-types
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)  # max_length = 50
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models. DateTimeField(auto_now=True)
    publish = models.DateTimeField(
        auto_now_add=False, auto_now=False, default=timezone.now)

    def save(self, wargs, **kwargs):

        if self.slug is None:
            self.slug = slugify(self.title)
        super(). save(wargs, **kwargs)

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
# Create your models here.
from .utils import slugify_instance_title


class Article(models.Model):
    # Django model-field-types
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True,
                            null=True)  # max_length = 50
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models. DateTimeField(auto_now=True)
    publish = models.DateTimeField(
        auto_now_add=False, auto_now=False, default=timezone.now)

    def save(self, *args, **kwargs):

        # if self.slug is None:
        #    self.slug = slugify(self.title)
        super().save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):

    # print("pre_save")
    print(sender, instance)

    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):

    # print('post_save')
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(article_post_save, sender=Article)

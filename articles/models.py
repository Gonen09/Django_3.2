from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils import timezone
# Create your models here.
from .utils import slugify_instance_title

User = settings.AUTH_USER_MODEL

class ArticleManager(models.Manager):
    def search(self, query=None):
        if query is None or query == "":
            return self.get_queryset().none()  # []
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.get_queryset().filter(lookups)


class Article(models.Model):
    # Django model-field-types
    user = models.ForeignKey(User, blank=True,
                             null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True,
                            null=True)  # max_length = 50
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models. DateTimeField(auto_now=True)
    publish = models.DateTimeField(
        auto_now_add=False, auto_now=False, default=timezone.now)

    objects = ArticleManager()

    def get_absolute_url(self):
        # return f'/articles/{self.slug}/'
        return reverse("article-detail", kwargs={"slug": self.slug})

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

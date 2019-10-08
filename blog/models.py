from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post_type_choices = [
        ('texto', 'Texto simples'),
        ('imagem', 'Imagem'),
        ('youtube', 'Vídeo do Youtube'),
    ]
    post_type = models.CharField(
        max_length=20,
        choices=post_type_choices,
        default='texto',
    )
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

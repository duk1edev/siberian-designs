from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, ResizeToFill


# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    thumb = ProcessedImageField(upload_to='works', processors=[ResizeToFill(400, 300)], format='JPEG',
                                options={'quality': 90})
    is_visible = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Example(models.Model):
    title = models.TextField(max_length=200, default='default')
    description = models.TextField(max_length=1000, default='default', verbose_name='Описание')
    image = ProcessedImageField(upload_to='works',
                                processors=[ResizeToFit(width=1280)],
                                format='JPEG',
                                options={'quality': 100})
    thumb = ProcessedImageField(upload_to='albums',
                                processors=[ResizeToFill(400, 500)],
                                format='JPEG',
                                options={'quality': 80})
    work = models.ForeignKey(Work, on_delete=models.PROTECT)
    alt = models.CharField(max_length=255)

    def __str__(self):
        return 'picture - ' + self.description + ' from ' + str(self.work)

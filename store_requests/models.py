from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class StoredRequest(models.Model):
    path = models.CharField(max_length=155)
    method = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)

    user_agent = models.CharField(max_length=255, blank=True, null=True)
    http_host = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=24, blank=True, null=True)
    referer = models.CharField(max_length=255, blank=True, null=True)

    is_ajax = models.BooleanField()
    is_secure = models.BooleanField()

    user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        verbose_name = 'stored request'
        verbose_name_plural = 'stored requests'
        ordering = ['-time', ]

    def __unicode__(self):
        return "{} {} at {}".format(self.method, self.path,
                                    self.time.strftime('%Y-%m-%d %H:%M:%S'))

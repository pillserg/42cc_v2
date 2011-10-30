from django.contrib.contenttypes.models import ContentType
from django.db import models


class ModelChange(models.Model):
    content_type = models.ForeignKey(ContentType)
    model_pk = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    event_choices = ((1, 'created'),
                     (2, 'updated'),
                     (3, 'deleted'),)

    event = models.IntegerField(choices=event_choices)


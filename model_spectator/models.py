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

    def __unicode__(self):
        return "{} {} {} {} {}".format(self.timestamp.isoformat(),
                                    self.get_event_display(),
                                    self.content_type.app_label,
                                    self.content_type.name,
                                    self.model_pk)


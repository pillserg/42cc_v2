from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save, post_delete


class ModelChange(models.Model):
    content_type = models.ForeignKey(ContentType)
    model_pk = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    event_choices = ((1, 'created'),
                     (2, 'updated'),
                     (3, 'deleted'),)

    event = models.IntegerField(choices=event_choices)

    class Meta:
        get_latest_by = 'timestamp'

    def __unicode__(self):
        return "{} {} {} {} {}".format(self.timestamp.isoformat(),
                                    self.get_event_display(),
                                    self.content_type.app_label,
                                    self.content_type.name,
                                    self.model_pk)


def add_db_entry_on_model_change(sender, instance, **kwargs):
    """saves info on saved model in db due to
       post save signal
    """

    exclude_models_names = ('ModelChange', 'Session', 'Message',
                            'StoredRequest')

    # do not save django models
    if sender._meta.app_label.startswith('django'):
        return
    # do not save ModelChange and some other stuff
    if sender.__name__ in exclude_models_names:
        return

    convertor = {True: 1, False: 2, 3: 3}
    event = convertor[kwargs.get('created', 3)]
    content_type = ContentType.objects.get_for_model(sender)

    ModelChange.objects.create(content_type=content_type,
                               model_pk=instance.pk,
                               event=event)

post_save.connect(add_db_entry_on_model_change)
post_delete.connect(add_db_entry_on_model_change)

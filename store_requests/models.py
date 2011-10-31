import datetime

from django.db import models
from django.contrib.auth.models import User


class CustomManager(models.Manager):
    """
    Adds get_or_none and get_firs_or_none method to objects,
    raises Exception if multiple objects returned
    """

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None

    def get_first_or_none(self, **kwargs):
        """
        Something like this can be achived by latest() qs method
        but this feels more flexible
        """
        qset = self.filter(**kwargs)
        try:
            return qset[0]
        except IndexError:
            return None

    def update_priority_by_ip(self, ip, priority=1):
        self.filter(remote_ip=ip).update(priority=priority)

    def update_priority_by_path(self, path, priority=1):
        self.filter(path=path).update(priority=priority)


class StoredRequest(models.Model):
    """
    Stored request representation
    """
    # I've experienced some problems with Ip field in the past,
    # thus generic CharField must do ok.
    remote_ip = models.CharField(default='undefined', max_length=100)
    path = models.CharField(max_length=155)
    method = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)

    user_agent = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=24, blank=True, null=True)
    referer = models.CharField(max_length=255, blank=True, null=True)

    is_ajax = models.BooleanField()
    is_secure = models.BooleanField()

    user = models.ForeignKey(User, blank=True, null=True)

    priority = models.IntegerField(default=1)
    ip_priority = models.IntegerField(default=0)
    path_priority = models.IntegerField(default=0)

    objects = CustomManager()

    class Meta:
        verbose_name = 'stored request'
        verbose_name_plural = 'stored requests'
        ordering = ['-time', ]

    @classmethod
    def parse_request(cls, request):
        """
        converts request to dictionary sutable for testing and
        creation of actual instance
        """
        parsed_request = dict(
            remote_ip=request.META.get('REMOTE_ADDR', 'undefined'),
            method=request.method,
            path=request.path,
            user_agent=request.META.get('HTTP_USER_AGENT', 'undefined'),
            language=request.META.get('LANGUAGE', 'en'),
            referer=request.META.get('HTTP_REFERER '),
            is_ajax=request.is_ajax(),
            is_secure=request.is_secure(),
                              )
        # Mock request has some problems with session so little hack here
        # also if app is used in environment without session middleware
        # it also may become handy.
        try:
            user = request.user
        except Exception:
            user = None
        else:
            if user.is_anonymous():
                user = None

        parsed_request['user'] = user
        return parsed_request

    def get_full_html_description(self):
        """
        __unicode__ returns only basic request chars, this will return full
        description.
        """
        html = ("Request from {} to {} at {}; method: {}; "
                "User_agent: {}; is_ajax: {}; is_secure: {}; "
                "language: {}; "
                "user: {}").format(self.remote_ip, self.path,
                                   self.time.strftime('%Y-%m-%d %H:%M:%S'),
                                   self.method, self.user_agent, self.is_ajax,
                                   self.is_secure, self.language, self.user)
        return html

    def __unicode__(self):
        return '{} {} "{}" at {}'.format(self.remote_ip, self.method,
                                         self.path,
                                         self.time.strftime('%Y-%m-%d'
                                                            ' %H:%M:%S'))

from django.contrib import admin

from models import StoredRequest


class StoredRequestAdmin(admin.ModelAdmin):
    list_display = ('time', 'remote_ip', 'method', 'path', 'user',
                    'is_ajax', 'is_secure', 'priority')
    list_editable = ('priority',)

admin.site.register(StoredRequest, StoredRequestAdmin)

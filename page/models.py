from django.db import models
from django.utils import timezone

from customer.models import Customer
from center.rq import Info
import configs.facebook as fb
import configs.facebook.mission
import configs.facebook.field


class Page(models.Model):
    STATUS_DISABLE = 'disable'
    STATUS_PUBLISH = 'publish'
    STATUS_CHOICE_FIELD = (
        (STATUS_PUBLISH, 'Kích hoạt'),
        (STATUS_DISABLE, 'Không kích hoạt')
    )

    name = models.CharField(max_length=255, blank=False, null=False)
    status = models.CharField(choices=STATUS_CHOICE_FIELD,
                              max_length=10,
                              default=STATUS_DISABLE)
    fb_id = models.CharField(max_length=50, null=True, unique=True)
    access_token = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    fan_count = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='page/', blank=True, null=True)
    customers = models.ManyToManyField(Customer, related_name='pages')

    def __str__(self):
        return str(self.name)

    @staticmethod
    def get_info_page(long_live_accses_token):
        access_token = long_live_accses_token
        fields = fb.field.PAGE_INFO
        mission = fb.mission.PAGE_INFO
        request = Info(access_token, mission, fields)
        response = request.get_response()
        return response


class Feed(models.Model):
    fb_id = models.CharField(unique=True, max_length=50, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    # attachments = models.TextField(null=True, blank=True)
    permalink_url = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(null=False, blank=False, default=timezone.now)
    page = models.ForeignKey(Page, null=True, blank=True,
                             related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return str((self.message, self.page))

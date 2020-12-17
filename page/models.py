from django.db import models
from django.utils import timezone
from enumfields import Enum, EnumField
from customer.models import Customer
from center.rq import Info
import configs.facebook as fb
import configs.facebook.mission
import configs.facebook.field
from django.utils.translation import ugettext_lazy as _


class PageStatus(Enum):
    STATUS_PUBLISH = _('publish')
    STATUS_DISABLE = _('disable')

    class Labels:
        STATUS_PUBLISH = _('Kích hoạt')
        STATUS_DISABLE = _('Không kích hoạt')


class Page(models.Model):
    status = EnumField(PageStatus, default=PageStatus.STATUS_DISABLE, verbose_name=_('status'))

    name = models.CharField(max_length=255, blank=False, null=False)
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

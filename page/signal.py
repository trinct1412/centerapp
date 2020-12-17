from django.db.models.signals import post_save
from django.dispatch import receiver
from customer.models import Customer
from page.models import Page
import logging


@receiver(post_save, sender=Customer)
def create_user_customer(sender, instance, created, **kwargs):
    if created:
        user = instance
        pages = []

        try:
            pages = Page.get_info_page(user.access_token).json().get("data")
        except Exception as e:
            logging.getLogger('get_api').warning(e)
        for page in pages:
            if page.get("id"):
                p = Page()
                p.fb_id = page.get("id")
                p.name = page.get("name")
                p.access_token = page.get("access_token")
                p.fan_count = page.get("fan_count")
                p.save()
                p.customers.add(user)
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

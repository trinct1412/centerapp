from django.db import models
from django.contrib.auth.models import User
from center.rq import Info
from center.rq import BaseRequest as rQ
import configs.facebook as fb
import configs.facebook.params
import configs.facebook.mission
import configs.facebook.field
import logging


class Customer(User):
    """
    username(unique)
    fist_name,last_name
    email
    is_staff==false,is_active==true has default
    """
    access_token = models.TextField(blank=True, null=True)
    fb_id = models.CharField(max_length=50,
                             unique=True,
                             blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    expires_in = models.IntegerField(blank=True, null=True)
    is_valid_access_token = models.BooleanField(default=False)
    shorted_access_token = models.TextField(blank=True, null=True)

    @property
    def full_name(self):
        return " ".join([self.last_name, self.first_name])

    @staticmethod
    def get_access_token(shorted_access_token):
        request = rQ(fb.mission.OAUTH_ACCESS_TOKEN)
        fb.params.USER_LONG_LIVE_ACESS_TOKEN['fb_exchange_token'] = shorted_access_token
        request.params = fb.params.USER_LONG_LIVE_ACESS_TOKEN
        response = request.get_response()
        return response

    @staticmethod
    def get_info_user(shorted_access_token):
        access_token = shorted_access_token
        fields = fb.field.USER_INFO
        mission = fb.mission.USER_INFO
        request = Info(access_token, mission, fields)
        response = request.get_response()
        return response

    def build_long_live_access_token(self):
        # Save long access token for customer
        try:
            access_token = self.get_access_token(self.shorted_access_token)
            if access_token:
                access_token = access_token.json()
                self.access_token = access_token['access_token']
                self.is_valid_access_token = True
                self.expires_in = access_token.get('expires_in')
            # End
        except Exception as e:
            logging.getLogger('user_create').error(e)
            self.is_valid_access_token = False

    def save(self, *args, **kwargs):
        user_info = self.get_info_user(self.shorted_access_token).json()
        user_name = user_info.get('email')
        customer = Customer.objects.filter(username=user_name)
        self.build_long_live_access_token()
        if user_name and not customer:
            self.username = user_name.split("@")[0]
            # Save basic information for user
            self.fb_id = user_info['id']
            self.last_name = user_info['last_name']
            self.first_name = user_info['first_name']
            self.email = user_info['email']
            # end save
            return super().save(*args, **kwargs)
        if customer:
            return customer.save()

    def __str__(self):
        return str((self.username, self.full_name))

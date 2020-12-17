from django.http import HttpResponse
from django.shortcuts import redirect
from center.rq import BaseRequest as rQ
from customer.models import Customer
from configs.facebook.mission import OAUTH_ACCESS_TOKEN
from configs.facebook.params import SORTED_LIVE_ACCESS_TOKEN
from configs.facebook.config import DOMAIN, APP_ID


def call_back_direct(request):
    href = "https://www.facebook.com/v9.0/dialog/oauth?client_id={}&redirect_uri={}".format(APP_ID, DOMAIN)
    return redirect(href)


def create_customer(request):
    code = request.GET.get('code', '')
    rq = rQ(OAUTH_ACCESS_TOKEN)
    SORTED_LIVE_ACCESS_TOKEN['code'] = code
    rq.params = SORTED_LIVE_ACCESS_TOKEN
    response = rq.get_response().json()
    a = Customer()
    a.shorted_access_token = response.get('access_token')
    a.expires_in = response.get('expires_in')
    a.save()
    return HttpResponse(a)

# param get long live access token
from .config import APP_ID, APP_SECRET,DOMAIN

USER_LONG_LIVE_ACESS_TOKEN = {
    'client_id': APP_ID,
    'client_secret': APP_SECRET,
    'grant_type': 'fb_exchange_token',
    'fb_exchange_token': ''}

SORTED_LIVE_ACCESS_TOKEN = {
    "client_id": APP_ID,
    "redirect_uri": DOMAIN,
    "client_secret": APP_SECRET,
    "code": ""
}

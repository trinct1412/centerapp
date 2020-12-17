from center.settings import DEBUG

"""configs facebook"""
GRAPH_API_VERSION = 'v9.0'
APP_ID = '2586040028170400'
APP_SECRET = 'fbdf2f3366974aca738d782e1be4a259'
DOMAIN = 'https://centerapp-network.herokuapp.com/'
if DEBUG:
    DOMAIN = "https://ce5fba2a0eb2.ngrok.io/"

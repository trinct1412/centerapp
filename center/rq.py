import requests
import json
import logging
from configs.facebook.href import GRAPH
from abc import ABC, abstractmethod


class BaseRequest(ABC):
    params = {}

    def __init__(self, mission):
        self.mission = mission
        self.url = GRAPH + self.mission

    def get_response(self):
        response = requests.get(url=self.url, params=self.params)
        if 'error' in response.json():
            log_data = {
                'method': 'GET',
                'status': response.status_code,
                'class': self.__class__.__name__,
                'url': response.url,
                'response': json.dumps(response.json())
            }
            message = "METHOD={method}\nSTATUS={status}\n" \
                      "CLASS={class}\nURL={url} \n" \
                      "RESPONSE={response}\n".format(**log_data)
            logging.getLogger('get_api').warning(message)
        return response


class Info(BaseRequest):
    def __init__(self, access_token, mission, fields):
        super(Info, self).__init__(mission)
        self.fields = fields
        self.url += "?fields=" + self.fields
        Info.params = {"access_token": access_token}

    def add_field(self, field):
        self.url += "," + field
        return self.url

    def set_field(self, fields, is_new_params=False):
        self.url += "," + ",".join(fields)
        if is_new_params:
            self.url += self.mission + "?fields=" + ",".join(fields)
        return self.url

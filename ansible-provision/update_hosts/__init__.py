# -*- coding: utf-8 -*-
import json
import requests
import sys


class Base(object):

    def __init__(self, service_settings):
        self.service_settings = service_settings
        self.api_key = service_settings['api_key']
        self.endpoint = service_settings['endpoint']
        self.dynamic_host_file = service_settings['dynamic_host_file']

    @property
    def headers(self):
        """Get the headers for each request
        """
        headers = {}
        for key, value in self.service_settings['headers'].iteritems():
            headers[key] = value

        # Digital Ocean
        if self.service_settings['name'] == 'digitalocean':
            headers['Authorization'] = headers['Authorization'] % self.api_key

        return headers

    @property
    def auth(self):
        if self.service_settings['auth'] is None:
            return None

        # Set the API Key, user is already set
        return (
            self.service_settings['auth']['user'],
            self.api_key
        )


    def _get(self, uri):
        """Make a GET request to the API
        """
        result = requests.get(
            self.endpoint % uri,
            headers=self.headers,
            timeout=60,
            auth=self.auth,
        )
        return result


    def _post(self, uri, data=None):
        """Make a POST request to the API
        """
        result = requests.post(
            self.endpoint % uri,
            data=json.dumps(data),
            headers=self.headers,
            timeout=60,
            auth=self.auth,
        )
        return result

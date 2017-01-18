#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import requests
import json

from update_hosts.dockercloud_client import DockerCloud


# --------------------------------------------------------------
# Commands
# --------------------------------------------------------------
dockercloud = {
    'name': 'dockercloud',
    'api_key': "docker_api_key_here",
    'endpoint': "https://cloud.docker.com/%s",
    'headers': {
        'Host': 'cloud.docker.com',
        'Accept': 'application/json'
    },
    'auth': {
        'user': 'iteamnetworkdc',
        'pass': 'e1b232b3-e398-4133-b5b6-7d77d1822bf0'
    },
    'dynamic_host_template': './hosts_template',
    'dynamic_host_file': './hosts',
    'markdown_file': '../HOSTS.md'
}

obj = DockerCloud(dockercloud)
obj.write_dynamic_hosts()

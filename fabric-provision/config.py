# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# Settings for each Service
# --------------------------------------------------------------
ssh_key = '~/.ssh/id_rsa.pub'
ssh_key_default = '~/.ssh/id_rsa.pub'

dockercloud = {
    'name': 'dockercloud',
    'api_key': "dockercloud_api_key_here",
    'endpoint': "https://cloud.docker.com/%s",
    'headers': {
        'Host': 'cloud.docker.com',
        'Accept': 'application/json'
    },
    'auth': {
        'user': 'docker_cloud_username',
        'pass': None, # use api_key
    },
    'dynamic_host_file': './dynamic_hosts/dockercloud.py',
}


digitalocean = {
    'name': 'digitalocean',
    'api_key': "digitalocean_api_key_here",
    'endpoint': "https://api.digitalocean.com/v2/%s",
    'headers': {
        'Content-Type': 'application/json',
        'Authorization': "Bearer %s", # use api_key
    },
    'auth': None,
    'dynamic_host_file': './dynamic_hosts/digitalocean.py',
}

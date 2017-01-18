#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import requests
import json
import config

import click

from client.digitalocean_client import DigitalOcean
from client.dockercloud_client import DockerCloud


# --------------------------------------------------------------
# Commands
# --------------------------------------------------------------
@click.group()
def cli():
    """Entry point from __main__ to call click commands below
    """
    pass


@click.command()
def digitalocean():
    obj = DigitalOcean(config.digitalocean)
    obj.write_dynamic_hosts()
    return


@click.command()
def dockercloud():
    obj = DockerCloud(config.dockercloud)
    obj.write_dynamic_hosts()
    return


cli.add_command(digitalocean)
cli.add_command(dockercloud)


if __name__ == '__main__':
    cli()
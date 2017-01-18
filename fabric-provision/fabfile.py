# -*- coding: utf-8 -*-
import os.path
import sys
from fabric.api import *
from fabric import tasks
from fabric.api import run
from fabric.api import env
from fabric.network import disconnect_all

import config

# Generated from app.py
try:
    from dynamic_hosts.digitalocean import ip_list
    #from dynamic_hosts.digitalocean import ip_list
except:
    print "You must generate the dynamic hosts from app.py"
    sys.exit()

# --------------------------------------------------------------
# Authentication
# --------------------------------------------------------------
env.user = 'root'

if os.path.isfile(config.ssh_key):
    env.key_filename = config.ssh_key
else:
    env.key_filename = config.ssh_key_default


# --------------------------------------------------------------
# Hosts
# --------------------------------------------------------------

env.hosts = ip_list
print env.hosts

# --------------------------------------------------------------
# Commands
# --------------------------------------------------------------
@parallel
def test():
    print "(+) Running test"
    run("ls")
    print "(+) Finished test"

@parallel
def update():
    print "(+) Running apt-get update"
    run("apt-get update")
    print "(+) Finished apt-get update"
    # disconnect_all()

@parallel
def upgrade():
    print "(+) Running apt-get upgrade"
    run("apt-get upgrade -y")
    print "(+) Finished apt-get upgrade"

@parallel
def autoclean():
    run("apt-get autoclean")

@parallel
def autoremove():
    run("apt-get autoremove -y")

@parallel
def unattended_upgrades():
    run("apt-get install unattended-upgrades -y")
    run("dpkg-reconfigure unattended-upgrades")

@parallel
def security():
    """Install Security Items
    """
    run("""apt-get install -y \
        rkhunter\
        clamav
        """)

    # Update RKHunter
    run("rkhunter --update --quiet")

    # Start FreshClam (Checks for updates 24 times a day)
    # eg: grep -i check /etc/clamav/freshclam.conf
    run("/etc/init.d/clamav-freshclam start")

    mkdir("/root/cron")
    """ RKHunter: Update Definitions Hourly """
    run('echo "* * * * 0 rkhunter --update --quiet >> /root/cron/rkhunter_update')
    run('crontab /root/cron/rkhunter_update')

@parallel
def utils():
    """Installs utilties
    """
    run("""apt-get install -y \
            at\
            htop\
            git\
            tree\
            whois\
            xclip\
            vim
        """)
    # Do NOT have a trailing slash on the last item

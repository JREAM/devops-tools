# -*- coding: utf-8 -*-
import json
import requests
import sys
from . import Base


class DigitalOcean(Base):

    def __init__(self, service_settings):
        super(DigitalOcean, self).__init__(service_settings)

    def list_droplets(self, per_page=100):
        """List all droplets you have
        """
        return self._get("droplets?page=1&per_page=%s" % per_page)

    def write_dynamic_hosts(self):
        """Writes a dynamic host python file for use in fabric
        """
        r = self.list_droplets()

        # print r.text

        f = open(self.service_settings['dynamic_host_file'], 'w')

        # Start a Python List
        f.write("ip_list = [\n")

        # --------------------------------------------------------------
        # Parse the data
        # --------------------------------------------------------------
        data = r.json()
        for obj in data['droplets']:
            print obj['networks']['v4'][0]['ip_address']

            # Save IP to file
            f.write("\t'" + obj['networks']['v4'][0]['ip_address'] + ":22'," + "\n")

        f.write(']') # Close the List
        f.close()

        print "Done"

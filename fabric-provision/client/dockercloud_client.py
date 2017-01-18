# -*- coding: utf-8 -*-
import json
import requests
import sys
from . import Base


class DockerCloud(Base):

    def __init__(self, service_settings):
        super(DockerCloud, self).__init__(service_settings)

    def service(self):
        """ List all available DockerCloud services
        """
        return self._get('api/app/v1/service/')

    def get_nodes(self):
        """ List all available Nodes running
        """
        return self._get('api/infra/v1/node/')

    def write_dynamic_hosts(self):
        """Writes a dynamic host python file for use in fabric
        """
        search_tag = raw_input("Searching for a specific tag? [Default: None]: ")
        r = self.get_nodes()

        f = open(self.service_settings['dynamic_host_file'], 'w')

        # Start a Python List
        f.write("ip_list = [\n")

        # --------------------------------------------------------------
        # Parse the data
        # --------------------------------------------------------------
        data = r.json()
        for obj in data['objects']:
            if not search_tag:
                print "Node IP: %s" % obj['public_ip']
                print "State: %s" % obj['state']
                print "Uuid: %s" % obj['uuid']

                # Save IP to file
                f.write("\t'" + obj['public_ip'] + ":22'," + "\n")

                for tag in obj['tags']:
                    print "Tag: " + str(tag['name'])
                print "\n"
            else:
                for tag in obj['tags']:
                    if search_tag and search_tag == tag['name']:
                        print "Node IP: %s" % obj['public_ip']
                        print "State: %s" % obj['state']
                        print "Uuid: %s" % obj['uuid']

                        # Save IP to file
                        f.write("\t'" + obj['public_ip'] + ":22'," + "\n")

                        for tag in obj['tags']:
                            print "Tag: " + str(tag['name'])
                    print "\n"

        f.write(']') # Close the List
        f.close()

        print "Done"

# -*- coding: utf-8 -*-
import sys
import re
import json
import time
import requests
from . import Base


class DockerCloud(Base):

    """ These are for knowing when to write [dockercloud_servers:development]
        or the production value only once into the file for sub-groups.
    """
    child_production_written = False
    child_development_written = False

    def __init__(self, service_settings):
        super(DockerCloud, self).__init__(service_settings)

    def get_nodes(self):
        """ List all available Nodes running
        """
        return self._get('api/infra/v1/node/')

    def write_dynamic_hosts(self):
        """Writes a into the hosts file for new/removed docker-cloud servers
        """
        r = self.get_nodes()

        # --------------------------------------------------------------
        # Parse the data
        # --------------------------------------------------------------
        data = r.json()

        output_markdown = "# Docker Cloud Hosts\n"
        output_markdown += "Generated On: %s\n\n" % time.strftime("%m/%d/%Y")
        output_markdown += "| Node | IP |\n"
        output_markdown += "|---|---|\n"

        output_text = "[dockercloud_servers]\n"

        output_data = []

        for obj in data['objects']:

            # Sort the tags so they are easier to read
            sorted_tags = []
            for k in obj['tags']:

                # <Environment>-<Type>-<Location>
                if k['name'] == 'development' or k['name'] == 'production':
                    sorted_tags.insert(0, k['name'])

                # Should be the <Location>, ending in a digit is for nyc1, etc.
                elif re.search(r'\d+$', k['name']) is not None:
                    sorted_tags.insert(2, k['name'])

                # Should be the <Type>
                else:
                    sorted_tags.insert(1, k['name'])

            # Friendly Readable Tag Strings
            output_data.append({
                'tag': '-'.join(sorted_tags),
                'tags': sorted_tags,
                'host': obj['public_ip'],
                'state': obj['state'],
            })

        # Sort the list
        output_data = sorted(output_data, key=lambda k: k['tag'])

        # Organize and write the data
        for item in output_data:

            # Output in terminal for our own viewing.
            print "Name: %s" % item['tag']
            print "      IP:    %s" % item['host']
            print "      State: %s\n" % item['state']

            # The Ansible Data We Need in ./hosts
            output_text += "%s ansible_host=%s\n" % (item['tag'], item['host'])
            output_markdown += "| %s | %s |\n" % (item['tag'], item['host'])

        # --------------------------------------------------------------
        # Write the Updated Hosts File
        # --------------------------------------------------------------

        # One extra newline before the next [group] in hosts
        output_text += "\n"

        # Read the current Host Data into a string
        with open(self.service_settings['dynamic_host_template'], 'r') as f:
            hosts_data = f.read()
            hosts_new = re.sub(r'(?:\[dockercloud_servers\]){1}(?:[^ ]+)(?=\[)', output_text, hosts_data)

        with open(self.service_settings['dynamic_host_file'], 'w') as f:
            f.write(hosts_new)

        # --------------------------------------------------------------
        # Write an Updated HOSTS.md file
        # --------------------------------------------------------------
        with open(self.service_settings['markdown_file'], 'w') as f:
            f.write(output_markdown)
            print "\n(+) Completed. ../HOSTS.md updated for user friendly reading"

        # Operations Complete
        print "\n(+) Completed: ./hosts updated for [dockercloud_servers]"

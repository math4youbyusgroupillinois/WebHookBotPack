#!/usr/bin/env python
"""
Build script for the plugin
"""
from optparse import OptionParser
import os
import re
from setuptools import setup
from subprocess import call
import sys
import shutil

####
## User Settings
####


package_name = 'botfactory_webhook'
package_version = '16.1.0'
package_description = 'Webhook action for BotFactory'


def create_package():

    setup(
        name=package_name
        ,version=package_version
        ,description=package_description
        ,author='Divvy Corp.'
        ,author_email='developers@divvycloud.com'
        ,platforms=['any']
        ,license='(c)2016 Divvy Corp.'
        ,keywords = "divvycloud plugins"
        ,zip_safe = False
        ,url = "https://www.divvycloud.com"
        ,packages = ["botfactory_webhook"]
        ,package_dir={"botfactory_webhook" : "cooked/botfactory_webhook"}
        ,package_data = {"botfactory_webhook" : [
                                            'plugin.json']
                                            }
        ,entry_points = {"divvycloud.plugins" : 'plugin_entry = plugin:load'}
        ,classifiers = [
            "Development Status :: 4 - Beta",
            "Topic :: Utilities"
        ],
        test_suite = 'test'
    )


if __name__ == "__main__":
    # If dev mode 'build', don't build the egg, just run webpack
    dev_mode = False

    parser = OptionParser(usage='Usage: %prog [options]')
    parser.add_option('--override-version', dest='version', help='Specify an explicit version for this package which overrides the current default of [{0}]'.format(package_version))
    parser.add_option('--dev', action="store_true", default=False, dest='dev_mode', help='Perform a "dev" build, which does not build an egg, just runs webpack')
    (options, args) = parser.parse_args()

    # If no extra args are specified, use bdist_egg by default
    if not args:
        args = ["bdist_egg"]

    # Replace command line arguments with everything we didn't parse
    sys.argv = [ sys.argv[0] ]
    sys.argv.extend(args)

    # Set override version if defined
    if options.version is not None:
        package_version = options.version

    create_package()

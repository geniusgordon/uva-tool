#!/usr/bin/env python

import os
import ConfigParser

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.abspath(__file__ + '/../'), 'uva.ini'))


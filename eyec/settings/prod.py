import os
from eyec.settings.base import *

#Override for prod settings
DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com']

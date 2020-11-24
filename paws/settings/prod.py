import os
from paws.settings.base import * # pylint: disable=unused-wildcard-import

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SERCRET_KEY = os.environ["SECRET_KEY"]

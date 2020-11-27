from paws.settings.base import * # pylint: disable=unused-wildcard-import


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "notsecret"
ALLOWED_HOSTS = [
    "localhost",
    "pawsproject.ddns.net",
    "10.0.2.2"
]
import logging.handlers
import os

from funfactory.settings_base import *

PROJECT_MODULE = 'solitude'
MINIFY_BUNDLES = {}

# Defines the views served for root URLs.
ROOT_URLCONF = '%s.urls' % PROJECT_MODULE

INSTALLED_APPS = (
    'aesfield',
    'funfactory',
    'django_nose',
    'django_statsd',
    'solitude',
)

SOLITUDE_PROXY = os.environ.get('SOLITUDE_PROXY', 'disabled') == 'enabled'
if SOLITUDE_PROXY:
    # The proxy runs with no database access. And just a couple of libraries.
    INSTALLED_APPS += (
        'lib.proxy',
    )
else:
    # If this is the full solitude instance add in the rest.
    INSTALLED_APPS += (
        'lib.buyers',
        'lib.sellers',
        'lib.transactions'
    )

TEST_RUNNER = 'test_utils.runner.RadicalTestSuiteRunner'

MIDDLEWARE_CLASSES = (
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.common.CommonMiddleware'
)

SESSION_COOKIE_SECURE = True

# PayPal values.
PAYPAL_APP_ID = ''
PAYPAL_AUTH = {'USER': '', 'PASSWORD': '', 'SIGNATURE': ''}
PAYPAL_CHAINS = ()
PAYPAL_CERT = None
PAYPAL_LIMIT_PREAPPROVAL = True
PAYPAL_URL_WHITELIST = ()
PAYPAL_USE_SANDBOX = True

# Access the cleansed settings values.
CLEANSED_SETTINGS_ACCESS = False

LOGGING = {
    'filters': {},
    'formatters': {},
    'handlers': {
        'unicodesyslog': {
            '()': 'solitude.settings.log.UnicodeHandler',
            'facility': logging.handlers.SysLogHandler.LOG_LOCAL7,
            'formatter': 'prod',
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
    },
    'loggers': {
        's': {
            'handlers': ['unicodesyslog'],
            'level': 'INFO',
        },
        'sentry.errors': {
            'handlers': ['unicodesyslog'],
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['unicodesyslog', 'sentry'],
            'level': 'INFO',
        },
    },
}

METLOG_CONF = {
    'logger': 'solitude',
    'sender': {
        'class': 'metlog.senders.logging.StdLibLoggingSender',
    },
}

# These are the AES encryption keys for different fields.
AES_KEYS = {
    'buyerpaypal:key': '',
    'sellerpaypal:id': '',
    'sellerpaypal:token': '',
    'sellerpaypal:secret': '',
}

DUMP_REQUESTS = False

"""
Development settings
"""
import os

from website.settings.base import Base

__all__ = ['Development']


class Development(Base):
    DEBUG = True

    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DB_DEFAULT_NAME'),
            'HOST': os.environ.get('DB_DEFAULT_HOST'),
            'PORT': os.environ.get('DB_DEFAULT_PORT'),
            'USER': os.environ.get('DB_DEFAULT_USER'),
            'PASSWORD': os.environ.get('DB_DEFAULT_PASSWORD'),
        },
    }

    CLINNER_DEFAULT_ARGS = {
        'runserver': '0.0.0.0:8000',
        'passenger': '--environment development '
                     '--log-file /srv/apps/{{ cookiecutter.project_slug }}/logs/passenger.log '
                     '--python python3.6 '
                     '--app-type wsgi '
                     '--startup-file website/wsgi.py',
        'unit_tests': '--no-input',
    }

    @classmethod
    def pre_setup(cls):
        super(Development, cls).pre_setup()

        os.environ['DJANGO_SECRET_KEY'] = os.environ.get('DJANGO_SECRET_KEY', '1234567890')

        cls.REQUEST_LOGGING_EXCLUDE[''] += (r'{}'.format(cls.STATIC_URL),)

        for handler, props in cls.LOGGING['handlers'].items():
            props['level'] = 'DEBUG'

        for logger, props in cls.LOGGING['loggers'].items():
            props['level'] = 'DEBUG'

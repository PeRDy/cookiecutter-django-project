#!/usr/bin/env python3.6
"""Run script.
"""
import argparse
import os
import shlex
import sys
from typing import List

import configurations.importer
from clinner.command import Type as CommandType, command
from clinner.run.main import HealthCheckMixin, Main as ClinnerMain

PYTHON = 'python3.6'
COVERAGE = 'coverage'
PROSPECTOR = 'prospector'
HEALTH_CHECK = 'health_check'
PASSENGER = 'passenger'


class Main(HealthCheckMixin, ClinnerMain):
    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument('-s', '--settings', help='Settings class',
                            default='{{ cookiecutter.app_slug }}.settings:Development')

    def inject_app_settings(self):
        """
        Injecting own settings.
        """
        host = os.environ.get('APP_HOST', '0.0.0.0')
        port = os.environ.get('APP_PORT', '8000')

        os.environ['APP_HOST'] = host
        os.environ['APP_PORT'] = port
        os.environ['DJANGO_SETTINGS_MODULE'], os.environ['DJANGO_CONFIGURATION'] = self.settings.rsplit(':', 1)
        os.environ['HEALTH_CHECK_SETTINGS'] = self.settings

        # Mark django-configurations as installed to avoid setup error
        configurations.importer.install()

    def health_check(self):
        """
        Does a check using Health Check application.

        :return: 0 if healthy.
        """
        return not self.run_command('manage', 'health_check', 'health', '-e')


@command(command_type=CommandType.SHELL,
         parser_opts={'help': 'Run gulp'})
def gulp(*args, **kwargs) -> List[List[str]]:
    cmd = ['gulp']
    cmd += args
    return [cmd]


@command(command_type=CommandType.SHELL,
         parser_opts={'help': 'Django manage commands'})
def manage(*args, **kwargs) -> List[List[str]]:
    cmd = shlex.split(f'{PYTHON} manage.py')
    cmd += args
    return [cmd]


@command(command_type=CommandType.SHELL,
         parser_opts={'help': 'Apply django migrations'})
def migrate(*args, **kwargs) -> List[List[str]]:
    return manage('migrate', *args)


@command(command_type=CommandType.SHELL,
         parser_opts={'help': 'Django collect statics'})
def collectstatic(*args, **kwargs) -> List[List[str]]:
    return manage('collectstatic', *args)


@command(command_type=CommandType.SHELL_WITH_HELP,
         parser_opts={'help': 'Migrate and collect statics'})
def build(*args, **kwargs) -> List[List[str]]:
    npm = shlex.split('npm install')
    return [npm] + gulp('default:dist') + migrate('--fake-initial') + collectstatic('--noinput')


@command(command_type=CommandType.SHELL,
         parser_opts={'help': 'Run prospector lint'})
def prospector(*args, **kwargs) -> List[List[str]]:
    cmd = [PROSPECTOR]
    cmd += args
    return [cmd]


@command(command_type=CommandType.SHELL,
         parser_opts={'help': 'Run development server'})
def runserver(*args, **kwargs) -> List[List[str]]:
    return migrate('--fake-initial') + manage('runserver', *args)


@command(command_type=CommandType.SHELL_WITH_HELP,
         parser_opts={'help': 'Run production server'})
def passenger(*args, **kwargs) -> List[List[str]]:
    cmd = [PASSENGER, 'start']
    cmd += ['--address', os.environ['APP_HOST'], '--port', os.environ['APP_PORT']]
    cmd += args
    return gulp('default:dist') + migrate('--fake-initial') + collectstatic('--noinput') + [cmd]


@command(command_type=CommandType.SHELL,
         parser_opts={'help': 'Django shell'})
def shell(*args, **kwargs) -> List[List[str]]:
    return manage('shell_plus', *args)


if __name__ == '__main__':
    main = Main()
    sys.exit(main.run())

#!/usr/bin/env python3.6
"""Run script.
"""
import argparse
import os
from typing import List

import configurations.importer
from clinner.command import Type as CommandType, command
from clinner.run.main import HealthCheckMain

PYTHON = 'python3.6'
COVERAGE = 'coverage'
PROSPECTOR = 'prospector'
HEALTH_CHECK = 'health_check'
PASSENGER = 'passenger'


class Main(HealthCheckMain):
    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument('-s', '--settings', default='website.settings:Development', help='Settings class')

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


@command(command_type=CommandType.SHELL)
def gulp(*args, **kwargs) -> List[List[str]]:
    cmd = ['gulp']
    cmd += args
    return [cmd]


@command(command_type=CommandType.SHELL)
def manage(*args, **kwargs) -> List[List[str]]:
    cmd = shlex.split(f'{PYTHON} manage.py')
    cmd += args
    return [cmd]


@command(command_type=CommandType.SHELL)
def migrate(*args, **kwargs) -> List[List[str]]:
    return manage('migrate', *args)


@command(command_type=CommandType.SHELL)
def collectstatic(*args, **kwargs) -> List[List[str]]:
    return manage('collectstatic', *args)


@command(command_type=CommandType.SHELL)
def build(*args, **kwargs) -> List[List[str]]:
    npm = shlex.split('npm install')
    return [npm] + gulp('default:dist') + migrate('--fake-initial') + collectstatic('--noinput')


@command(command_type=CommandType.SHELL)
def prospector(*args, **kwargs) -> List[List[str]]:
    cmd = [PROSPECTOR]
    cmd += args
    return [cmd]


@command(command_type=CommandType.SHELL)
def runserver(*args, **kwargs) -> List[List[str]]:
    return migrate('--fake-initial') + manage('runserver', *args)


@command(command_type=CommandType.SHELL)
def passenger(*args, **kwargs) -> List[List[str]]:
    cmd = [PASSENGER, 'start']
    cmd += ['--address', os.environ['APP_HOST'], '--port', os.environ['APP_PORT']]
    cmd += args
    return gulp('default:dist') + migrate('--fake-initial') + collectstatic('--noinput') + [cmd]


@command(command_type=CommandType.SHELL)
def shell(*args, **kwargs) -> List[List[str]]:
    return manage('shell_plus', *args)


if __name__ == '__main__':
    main = Main()
    sys.exit(main.run())

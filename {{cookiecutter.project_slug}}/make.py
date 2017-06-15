#!/usr/bin/env python3
import os
import shlex
import sys

try:
    from clinner.command import command, Type as CommandType
    from clinner.run import Main
except ImportError:
    import pip

    print('Installing Clinner')
    pip.main(['install', '--user', '-qq', 'clinner'])

    from clinner.command import command, Type as CommandType
    from clinner.run import Main

DOCKER_IMAGE = '{{ cookiecutter.project_slug }}'


@command(command_type=CommandType.SHELL_WITH_HELP,
         args=((('--registry',), {'help': 'Docker registry'}),
               (('--name',), {'help': 'Docker image name', 'default': DOCKER_IMAGE}),
               (('--tag',), {'help': 'Docker image tag', 'default': 'latest'})),
         parser_opts={'help': 'Docker build for local environment'})
def build(*args, **kwargs):
    tag = '{name}:{tag}'.format(**kwargs)
    if kwargs['registry']:
        tag = '{registry}/{tag}'.format(registry=kwargs['registry'], tag=tag)

    cmd = shlex.split('docker build -t {tag} .'.format(tag=tag))
    return [cmd]


@command(command_type=CommandType.SHELL_WITH_HELP, parser_opts={'help': 'Up application stack'})
def up(*args, **kwargs):
    cmd = shlex.split('docker-compose up -d')
    return [cmd]


@command(command_type=CommandType.SHELL_WITH_HELP, parser_opts={'help': 'Down application stack'})
def down(*args, **kwargs):
    cmd = shlex.split('docker-compose down')
    return [cmd]


@command(command_type=CommandType.SHELL_WITH_HELP, parser_opts={'help': 'Restart application stack'})
def restart(*args, **kwargs):
    cmd = shlex.split('docker-compose restart') + list(args)
    return [cmd]


@command(command_type=CommandType.SHELL_WITH_HELP,
         args=((('--format', ), {'default': 'text', 'help': 'Output format'}),),
         parser_opts={'help': 'Run unit tests'})
def prospector(*args, **kwargs):
    cmd = shlex.split(
        'docker-compose run app --skip-check --quiet prospector --output-format={}'.format(kwargs['format']))
    return [cmd]


@command(command_type=CommandType.SHELL_WITH_HELP, parser_opts={'help': 'Run unit tests'})
def unit_tests(*args, **kwargs):
    cmd = shlex.split('docker-compose run app -s contentkb_api.settings:UnitTests --skip-check --quiet unit_tests')
    return [cmd]


if __name__ == '__main__':
    sys.exit(Main().run())

#!/usr/bin/env python2
"""
Helper script to migrate environment variables between resin.io apps using
the SDK.
"""
import sys

import click
from resin import Resin

resin = Resin()

@click.command()
@click.option('--from', '-f', 'from_app', type=click.INT, required=True, help="ID of application to copy env vars from")
@click.option('--to', '-t', 'to_app', type=click.INT, required=True, help="ID of application to copy env vars to")
@click.option('--token', envvar='RESIN_TOKEN', required=True, help="Resin.io auth token, can specify it with the RESIN_TOKEN env var as well")
@click.option('--delete-extra', is_flag=True, help="Toggles deleting extra environment variables in the receiving app")
@click.option('--quiet', '-q', is_flag=True, help="Toggles hiding process details")
@click.confirmation_option(prompt='Are you sure you want to copy the env vars?')
def copy_env_vars(from_app, to_app, delete_extra, quiet, token):
    """Migrate environment variables from one resin.io app to another,
    optionally removing variables from the target that do not exist at the origin.
    """
    if from_app == to_app:
        print("Nothing to copy")
        sys.exit(0)
    resin.auth.login_with_token(token)
    if not quiet:
        print("Logged in user: {}".format(resin.auth.who_am_i()))

    # Get current environment variables
    envs2 = resin.models.environment_variables.application.get_all(to_app)
    envnames2 = {}
    for env in envs2:
        envnames2[env['name']] = env

    # Get variables to copy and proceed
    envs1 = resin.models.environment_variables.application.get_all(from_app)
    envnames1 = {}
    for env in envs1:
        envnames1[env['name']] = env
        if env['name'] in envnames2:
            if not quiet:
                print("Updating {} -> {}".format(env['name'], env['value']))
            resin.models.environment_variables.application.update(envnames2[env['name']]['id'], env['value'])
        else:
            if not quiet:
                print("Creating {} -> {}".format(env['name'], env['value']))
            resin.models.environment_variables.application.create(to_app, env['name'], env['value'])

    # Delete extra variables from the target if needed
    if delete_extra:
        env_delete = set(envnames2) - set(envnames1)
        for envname in env_delete:
            if not quiet:
                print("Deleting {}".format(envname))
            resin.models.environment_variables.application.remove(envnames2[envname]['id'])

if __name__ == "__main__":
    copy_env_vars()

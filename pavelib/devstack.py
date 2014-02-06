"""
Start servers in the Vagrant devstack VM.
"""

import argparse
from paver.easy import *
from .utils.process import run_process
from .utils.color import print_red
from .utils.cmd import django_cmd


DEFAULT_PORT = {"lms": 8000, "studio": 8001}


@task
@needs('pavelib.prereqs.install_prereqs')
@consume_args
def run_devstack(args):
    """
    Start the devstack lms or studio server
    """
    parser = argparse.ArgumentParser(prog='paver run_devstack')
    parser.add_argument('system', type=str, nargs=1, help="lms or studio")
    parser.add_argument('--fast', action='store_true', default=False, help="Skip updating assets")
    args = parser.parse_args(args)
    system = args.system[0]

    if system not in ['lms', 'studio']:
        print_red("System must be either lms or studio")
        exit(1)

    if not args.fast:
        call_task('pavelib.assets.update_assets', args=[system, "--settings=devstack"])

    run_process(django_cmd(
        system, 'devstack', 'runserver',
        "0.0.0.0:{}".format(DEFAULT_PORT[system])
    ))

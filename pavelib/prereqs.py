from paver.easy import *
import os
from distutils import sysconfig

import prereqs_cache

NPM_REGISTRY = "http://registry.npmjs.org/"
PYTHON_REQ_FILES = [
    'requirements/edx/pre.txt',
    'requirements/edx/base.txt',
    'requirements/edx/post.txt'
]


def install_ruby_prereqs():
    """
    Installs Ruby prereqs
    """
    if prereqs_cache.is_changed('ruby_prereqs', ['Gemfile']):
        sh('bundle install --quiet')
    else:
        print('Ruby requirements unchanged, nothing to install')


def install_node_prereqs():
    """
    Installs Node prerequisites
    """
    if prereqs_cache.is_changed('npm_prereqs', ['package.json']):
        sh("npm config set registry {}".format(NPM_REGISTRY))
        sh('npm install')
    else:
        print('Node requirements unchanged, nothing to install')


def install_python_prereqs():
    """
    Installs Python prerequisites
    """
    site_packages_dir = sysconfig.get_python_lib()

    requirements = prereqs_cache.get_files('requirements')

    if prereqs_cache.is_changed('requirements_prereqs', requirements, [site_packages_dir]):
        for req_file in PYTHON_REQ_FILES:
            sh("pip install -q --exists-action w -r {req_file}".format(req_file=req_file))

    else:
        print('Python requirements unchanged, nothing to install')


@task
def install_prereqs():
    """
    Installs Ruby, Node and Python prerequisites
    """
    install_ruby_prereqs()
    install_node_prereqs()
    install_python_prereqs()

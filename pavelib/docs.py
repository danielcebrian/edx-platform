import sys
import webbrowser
from paver.easy import *
from .utils.envs import Env


DOC_PATHS = {
    "dev": "docs/en_us/developers",
    "author": "docs/en_us/course_authors",
    "data": "docs/en_us/data",
    "default": "docs/en_us"
}


def _valid_doc_types():
    """
    Return a comma-separated string of valid doc types.
    """
    return ", ".join(DOC_PATHS.keys())


def _doc_path(options, allow_default=True):
    """
    Parse `options` (from the Paver task args) to determine the path
    to the documentation directory.
    If the specified path is not one of the valid options, print an error
    message and exit.

    If `allow_default` is False, then require that a type is specified,
    and exit with an error message if it isn't.
    """
    doc_type = getattr(options, 'type', 'default')
    path = DOC_PATHS.get(doc_type)

    if doc_type == 'default' and not allow_default:
        print "You must specify a documentation type using '--type'.  Valid options are: {options}".format(
            options=_valid_doc_types())
        sys.exit(1)

    if path is None:
        print "Invalid documentation type '{doc_type}'.  Valid options are: {options}".format(
            doc_type=doc_type, options=_valid_doc_types())
        sys.exit(1)

    else:
        return path


@task
@cmdopts([
    ("type=", "t", "Type of docs to compile"),
    ("verbose", "v", "Display verbose output"),
])
def build_docs(options):
    """
    Invoke sphinx 'make build' to generate docs.
    """
    verbose = getattr(options, 'verbose', False)

    cmd = "cd {dir}; make html quiet={quiet}".format(
        dir=_doc_path(options),
        quiet="false" if verbose else "true"
    )

    sh(cmd)


@task
@cmdopts([
    ("type=", "t", "Type of docs to show"),
])
def show_docs(options):
    """
    Show docs in browser
    """
    webbrowser.open('file://{root}/{path}/build/html/index.html'.format(
        root=Env.REPO_ROOT, path=_doc_path(options, allow_default=False)))


@task
@cmdopts([
    ("type=", "t", "Type of docs to compile"),
    ("verbose", "v", "Display verbose output"),
])
def doc(options):
    """
    Build docs and show them in browser
    """
    build_docs(options)
    show_docs(options)

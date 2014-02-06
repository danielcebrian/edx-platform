"""
Workspace migration tasks.
"""

import os
from paver.easy import *
from .utils.envs import Env


@task
def workspace_migrate():
    """
    Run scripts in ws_migrations directory
    """
    if os.getenv('SKIP_WS_MIGRATIONS', False):
        return

    MIGRATION_MARKER_DIR = Env.REPO_ROOT / '.ws_migrations_complete'
    MIGRATION_DIR = Env.REPO_ROOT / 'ws_migrations'

    files = os.listdir(MIGRATION_DIR)
    migration_files = []

    for file_handle in files:
        if not file_handle == 'README.rst' and os.access(file_handle, os.X_OK):
            migration_files.append(file_handle)

    for migration in migration_files:
        completion_file = MIGRATION_MARKER_DIR / migration.basename()
        if not completion_file.isfile():
            sh(MIGRATION_DIR / migration)
            open(completion_file, 'w')

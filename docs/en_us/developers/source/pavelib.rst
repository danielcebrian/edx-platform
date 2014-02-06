*******************************************
Paver
*******************************************


Paver provides a standardised way of managing development and operational tasks in edX.

To run individual commands, use the following syntax:

paver <command_name> --option=<option value>


Paver Commands
*******************************************

Paver commands are grouped as follows:

- Prereqs_ Install all of the prerequisite environments for Python, Node and Ruby
- Docs_ Docs is used to build and then optionally display the EdX docs relating to development, authoring and data management
- Assets_ Assets will compile Sass (CSS), Coffeescript (Javascript) and XModule assets. Optionally it can call Django’s collectstatic method
- `Run Servers`_ Run servers
- `Developer Stack`_ Management of developer Vagrant environment
- Workspace_ Migration utilities


.. _Prereqs:

Prereqs
=============

Install all of the prerequisite for Python, Node and Ruby

   **install_prereqs** : installs Ruby, Node and Python requirements

::

   paver install_prereqs

..


.. _Docs:

Docs
=============

Docs is used to build and then optionally display the EdX docs relating to development, authoring and data management

   **build_docs**:  Invoke sphinx 'make build' to generate docs.

    **--type=** <dev, author, data> Type of docs to compile

    **--verbose** Display verbose output

::

   paver build_docs --type=dev --verbose

..

   **show_docs**: Show docs in browser

    *--type=* <dev, author, data> Type of docs to compile

::

   paver show_docs --type=dev

..

   **doc**:  Invoke sphinx 'make build' to generate docs and then show in browser

    *--type=* <dev, author, data> Type of docs to compile

    *--verbose* Display verbose output

::

   paver doc --type=dev --verbose

..


.. _Assets:

Assets
=============

Assets will compile Sass (CSS), CoffeeScript (Javascript) and XModule assets. Optionally it can call Django's collectstatic command.


   **update_assets**: Compiles Coffeescript, Sass, Xmodule and optionally runs collectstatic

    *system* lms or studio

    *--settings=* Django settings e.g. aws, dev

    *--watch* Run in watch mode

    *--debug* Disable Sass compression

    *--collectstatic* Runs Django's collectstatic command

::

   paver compile_sass lms --settings=dev --watch --debug

..

.. _Run Servers:

Run Servers
=============

    **lms**: runs lms

     *--env=* Environment settings e.g. aws, dev

::

   paver lms --env=dev

..


    **cms**: runs cms

     *--env=* Environment settings e.g. aws, dev

::

   paver cms --env=dev

..

    **run_server**: run a specific server

     *--system=* System to act on e.g. lms, cms

     *--env=* Environment settings e.g. aws, dev

::

   paver run_server --system=lms --env=dev

..

    **resetdb**: runs syncdb and then migrate

     *--env=* Environment settings e.g. aws, dev

::

   paver resetdb --env=dev

..


    **check_settings**: checks settings files

     *--env=* Environment settings e.g. aws, dev

::

   paver check_settings --env=dev

..


    **run_all_servers**: runs lms, cms and celery workers

     *--env=* Environment settings e.g. aws, dev

     *--worker_env=* Environment settings for celery workers


::

   paver run_all_servers --env=dev --worker_env=celery

..


    **run_celery**: runs celery for specified system

     *--system=* System to act on e.g. lms, cms

     *--env=* Environment settings e.g. aws, dev

::

   paver run_celery --system=lms --env=dev

..

.. _Developer Stack:

Developer Stack
===============

Management of developer Vagrant environment


    **devstack**: Install prerequisites, compile assets and run the system specified

     *system*   lms or studio
     *--fast*   Skip updating assets

::

   paver devstack lms

..


.. _Workspace:

Workspace
=========

Migration tool to run arbitrary scripts


    **workspace_migrate**: Run scripts in ws_migrations directory

::

   paver workspace_migrate

..

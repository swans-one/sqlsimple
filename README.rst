SQL Simple
==========

Manage a project with a database, by just writing SQL. SQL Simple
provides the minimal tools required to interact with a database within
a python project. It's goal is to let the database itself do as much
of the work as possible.

Running Queries
---------------

Rather than use an ORM, sqlsimple simply uses SQL and returns
records. Provided you've setup your database making a query is as easy
as calling the ``sql`` function

.. code-block:: python

    from sqlsimple import sql

    results = sql("SELECT * FROM mytable")


Managing Your Database
----------------------

The power of sqlsimple comes mostly from its tools for helping you
manage the database. This library makes the following tasks a little
easier.

* Specifying a schema
* Schema migrations
* Data migrations
* Fixture loading
* Connection managment
* Trigger management
* Database view management
* Database function management

But you'll still use SQL! By using sqlsimple you can keep the code to
handle these database tasks in a central location, that is, along with
the rest of your application code.


License and Contributing
------------------------

All code is licensed under the MIT license. By making a pull request
to this repository you agree to contribute that code under the MIT
license, and ensure that you have the right to do so.

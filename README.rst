============
 REbus demo
============

About REbus demo agents
=======================


This repository shows a way to integrate a tool into the REbus ecosystem.

It comes with two simple tools implemented in
``string_tools.py`` and ``hash_tools.py`` files.

These tools are then wrapped into 2 agents (``stringer`` and ``hasher``).

Another agent (``grep``) will look for regular expressions into the output of the ``stringer`` agent.


In collaboration with some REbus agents (``inject``, ``link_finder`` and ``unarchive``) 


Agent ``stringer``
------------------

This agent accept ``/binary/`` descriptors in input, run ``/usr/bin/strings`` on it, 
and push one ``/string/`` descriptor per extracted string.


Agent ``hasher``
----------------

This agent accept ``/binary/`` descriptors in input and push their MD5.


Agent ``grep``
--------------

This agent will look for a regexp in all ``/string/`` descriptors and print it.

Running a demo
==============

In tool mode
------------

.. code::
 
 rebus_agent -m rebus_demo.agents hasher unarchive inject /tmp/foo.tgz -- return --short md5_hash


Should return something like

.. code::

 foo.tgz:bash = 5eaf5491c5b6c19f052989114ac70010
 foo.tgz:bunzip2 = a11e41edfe37b736dc098e08c0f008dd
 foo.tgz:bzip2recover = 8b57e17fa45c2e5f55cdbc6aa825f470
 foo.tgz:cat = cb230279212b1a85f7d6b8b7c9aadd9b
 foo.tgz:chacl = ebb0de6e2a2e3a24bd8d2a2db54a0414
 foo.tgz:chgrp = 990e6c7372a2502fdb94a3de224a4064
 foo.tgz:chmod = 2c5d1ebece7c36b5e0ddb6d3d784cd4f
 foo.tgz:chown = 5c29ac84a213cb87cbbbd9a767c84983
 foo.tgz:chvt = e7006732182a245d59a6e3d43576d2ae
 foo.tgz:cp = 4f799b30bb0d1f3c1509d328d65446e5
 foo.tgz:cpio = ef0e14ae9cf0dc8f54019530fcccf523


In infrastructure mode
----------------------

First we have to launch the bus master and the agents we want to work with:

.. code::

 rebus_master dbus &
 for agent in web_interface unarchive link_finder hasher stringer 
   do rebus_agent -m rebus_demo.agents --bus dbus $agent &
 done


Then we can inject a file with CLI (or with web interface):

.. code::

 rebus_agent --bus dbus inject /tmp/foo.tgz

Activity is visible on the web interface.

Finally we can use the ``grep`` agent to look for

.. code::

 rebus_agent --bus dbus -m rebus_demo.agents grep 12345 

.. code::

 foo.tgz:cpio = 0123456789ABCDEF
 foo.tgz:bash = 0123456789abcdef
 foo.tgz:bash = 0123456789ABCDEF

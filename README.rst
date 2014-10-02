CKAN OpenSpending
=================

A `CKAN <http://ckan.org>`__ extension which automatically uploads
budget data packages to the OpenSpending platform. This builds upon the
`ckanext-budgets <https://github.com/tryggvib/ckanext-budgets>`__
extensions which does the heavylifting of creating and marking resources
as budget data packages.

When a resource has been marked as a budget data package, this extension
will pick it up from there and submit it for automatic loading into
OpenSpending.

Installation
------------

Simply clone this library and run

::

    python setup.py install

Then add ``openspending`` to the list in ``ckan.plugins`` in your CKAN
configuration file. Restart your webserver and budget data will now be
automatically loaded for you.

Configuration
-------------

There are two required configurations which must be added to your CKAN
configuration file.

-  **ckan.site\_url** - The URL for the site
-  **openspending.apikey** - The API key for the user on OpenSpending
   which will be used to load the data

License
-------

Copyright (C) 2014 Open Knowledge Foundation

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see http://www.gnu.org/licenses/.

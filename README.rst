ArduinoDocs
===========

This is a tool to generate and publish online documentation for Arduino libraries. It uses Sphinx_,
Doxygen_ and Breathe_ to build documentation from the source code of your Arduino library and
publish it online on ReadTheDocs_.

You just need to follow these steps:

1. Install Python_ 2.7
2. Add documentation to your Arduino library using the `Doxygen standard`_
3. Copy ``arduinodocs.py`` to the root directory of your library and run it
4. Push your library code to GitHub_ and add a README.rst
5. Publish it to ReadTheDocs_

   a. Click "Import a Project"
   b. Connect to your GitHub account if you haven't done it yet
   c. Click "Import from GitHub"
   d. Select you project and click "Create"

6. Wait for your online documentation to build automatically. Enjoy!

Every time you commit to your Github repository, the documentation will be automatically rebuilt by ReadTheDocs.

This repository itself has been set up as an Arduino library called ArduinoDocs (see ``ArduinoDocs.h`` and ``ArduinoDocs.cpp``), and the documentation generated for it can be seen in http://arduinodocs.readthedocs.org/

If you want to build the documentation locally, you need to:

1. Install Sphinx_: ``pip install Sphinx``
2. Install Breathe_: ``pip install breathe``
3. Download and install Doxygen_
4. Run ``arduinodocs.py`` as above
5. ``cd`` to the ``docs`` directory
6. Run ``doxygen`` to extract the documentation from your source code
7. Run ``sphinx-build -b html . _build/html`` to generate the HTML documentation
8. Check documentation generated in ``_build/html``
   
.. _Sphinx: http://sphinx-doc.org/
.. _Doxygen: http://www.doxygen.org
.. _Breathe: http://breathe.readthedocs.org/
.. _ReadTheDocs: http://readthedocs.org/
.. _Python: http://python.org/
.. _`Doxygen standard`: http://www.stack.nl/~dimitri/doxygen/manual/docblocks.html
.. _GitHub: http://github.com/

----

Copyright (c) 2015 Circuitar
All rights reserved.

This software is released under an MIT license. See the attached LICENSE file for details.

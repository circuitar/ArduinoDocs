ArduinoDocs
===========

This is a tool to generate and publish online documentation for Arduino libraries. It uses Sphinx_,
Doxygen_ and Breathe_ to build documentation from the source code of your Arduino library and
publish it online on ReadTheDocs_.

* Source code: https://github.com/circuitar/ArduinoDocs
* Documentation: http://arduinodocs.readthedocs.org

Online Documentation
....................

To add online documentation to your library on ReadTheDocs_, you just need to follow these steps:

1. Install Python_
2. Add documentation to your Arduino library using the `Doxygen standard`_
3. Add a README.rst and make sure to add a :literal:`\-\-\-\-` transition somewhere. The README text will be
   included in the documentation up to that point.
4. Copy ``arduinodocs.py`` to the root directory of your library and run it
5. Push your library code to GitHub_
6. Publish it to ReadTheDocs_

   a. Click "Import a Project"
   b. Connect to your GitHub account if you haven't done it yet
   c. Click "Import from GitHub"
   d. Select you project and click "Create"
   e. Enter the project page in ReadTheDocs, click on ``Admin`` > ``Advanced Settings`` and use ``extras/docs/requirements.txt`` as the requirements file

7. Wait for your online documentation to build automatically. Enjoy!

Every time you push changes to your Github repository, the documentation will be automatically rebuilt by ReadTheDocs.

This repository itself has been set up as an Arduino library called ArduinoDocs (see ``ArduinoDocs.h`` and ``ArduinoDocs.cpp``). You can look at those files to see how to document your library code, and see how the auto-generated documentation looks in http://arduinodocs.readthedocs.org

Local Build
...........

If you want to build the documentation locally, you need to:

1. Install Sphinx_: ``pip install Sphinx``
2. Install Breathe_: ``pip install breathe``
3. Download and install Doxygen_
4. Follow the steps in the `Online Documentation`_ section up to the point where ``arduinodocs.py`` is run
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

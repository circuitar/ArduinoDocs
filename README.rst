ArduinoDocs
===========

This is a tool to create and publish online documentation for Arduino libraries. It uses Sphinx_,
Doxygen_ and Breathe_ to build documentation from the source code of your Arduino library and
publish it online on ReadTheDocs_.

1. Install Python_ 2.7
2. Add documentation to your Arduino library using the `Doxygen standard`_
3. Copy ``arduinodocs.py`` to the root directory of your library and run it
4. Push your library code to GitHub_
5. Sign up to ReadTheDocs_ and link it to your GitHub account
6. Create a project and link it to your GitHub repository
7. Enjoy your online documentation

Following the instructions above, ReadTheDocs will build all the documentation for you. If you want
to build it yourself, you need to:

1. Install _Sphinx: ``pip install Sphinx``
2. Install _Breathe: ``pip install breathe``
3. Downlosd and install _Doxygen
4. Run ``arduinodocs.py`` as above
5. ``cd`` to the ``docs`` directory
6. Run ``doxygen``
7. Run ``sphinx-build -b html . _build/html``
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

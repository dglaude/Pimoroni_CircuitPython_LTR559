Introduction
============

.. image:: https://readthedocs.org/projects/pimoroni_circuitpython_ltr559/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/pimoroni_circuitpython_ltr559/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/pimoroni/Pimoroni_CircuitPython_LTR559/workflows/Build%20CI/badge.svg
    :target: https://github.com/pimoroni/Pimoroni_CircuitPython_LTR559/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Library for the LTR559 Proximity/Presence/Light Sensor


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/pimoroni_circuitpython_ltr559/>`_. To install for current user:

.. code-block:: shell

    pip3 install pimoroni-circuitpython-ltr559

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install pimoroni-circuitpython-ltr559

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install pimoroni-circuitpython-ltr559

Usage Example
=============

.. code-block:: python

    import time
    from board import SCL, SDA
    from busio import I2C
    from pimoroni_circuitpython_ltr559 import Pimoroni_LTR559

    I2C_BUS = I2C(SCL, SDA)
    LTR559 = Pimoroni_LTR559(I2C_BUS)

    while True:
        print(LTR559.lux)  # Get Lux value from light sensor
        print(LTR559.prox)  # Get Proximity value from proximity sensor
        time.sleep(1.0)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/pimoroni/Pimoroni_CircuitPython_LTR559/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

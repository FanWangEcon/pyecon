Installation
============

Using github
------------

The easiest way to install ``pyecon`` is probably via ``github``:

.. code-block:: bash

    pip uninstall pyecon -y
    pip install git+https://github.com/fanwangecon/pyecon.git#egg=pyecon

This should also install dependencies if any are missing.

Using PyPI
----------

This should also work fine, version might be slightly behind:

.. code-block:: bash

    pip uninstall pyecon -y
    pip install pyecon

Other requirements
------------------

``pyecon`` builds on (and hence depends on) numpy`` and
``scipy`` libraries other packages shown in the
`toml file <https://github.com/FanWangEcon/pyecon/blob/master/doc/pyproject.toml>`_

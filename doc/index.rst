.. raw:: html

    <style type="text/css">

    .thumbnail {
        position: relative;
        float: left;
        margin: 10px;
        width: 160px;
        height: 160px;
    }

    .thumbnail img {
        position: absolute;
        display: inline;
        left: 0;
        width: 150px;
        height: 150px;
    }

    </style>

``pyecon``'s documentation
===========================

.. raw:: html

    <div style="clear: both"></div>
    <div class="container-fluid hidden-xs hidden-sm">
      <div class="row">
        <a href="auto_examples/plot_ff_gen_rgrid.html">
          <div class="col-md-2 thumbnail">
            <img src="_static/img/sphx_glr_plot_ff_gen_rgrid_001.svg">
          </div>
        </a>
      </div>
    </div>

``pyecon`` is a work-in-progress `package <https://pypi.org/project/pyecon/>`__
solving and estimating dynamic heterogeneous agents models. This package implements
solution concepts developed and used in several `projects <https://fanwangecon.github.io/research>`__
with dynamic asset choices with frictions. In addition, the `pyfan <https://github.com/FanWangEcon/pyfan>`__ repository
and the associated `package <https://pyfan.readthedocs.io/en/latest/>`__  contain
python support modules for dealing with data-structures and facilitating various research related-tasks.

Associated Papers
-----------------------

1. `An Empirical Equilibrium Model of Formal and Informal Credit Markets in Developing Countries <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3316939>`__


Solution and Estimation
-----------------------

There are five types of solution programs:

1. Static optimal choice
2. Dynamic optimal choice (and value function)
3. Endogenous distributions
4. Integration over exogenous types
5. Equilibrium market clearing

There are several types of estimation associated Programs:

1. Simulate given many parameters
2. Estimate and approximate objective function
3. Polynomial based concurrent minimization

Core and Support
----------------


Programs for Different Research Papers
--------------------------------------

.. toctree::
    :hidden:
    :maxdepth: 2

    quickstart
    user_guide/intertemporalmax
    reference
    auto_examples/index
    othersites

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

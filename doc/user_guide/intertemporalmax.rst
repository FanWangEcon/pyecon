Intertemporal Optimization
==========================

Maximize given value function. Given dynamic approximation, solve for optimal
choices (assets and consumption) given the trade-offs between contemporaneous
utility and expected future gains/losses from asset choices.

The maximization problem could be multi-staged, involving for example discrete
and continuous choices. First make continuous/discrete choices, then make
discrete/continuous choices. When the problem has sub-stages, solve backwards.

An generic intertemporal optimization problem could be written as below:

.. math::

    \max_{ x \in \Omega} u(c) + v(x)

    c = y - g\left(x\right)

Income is :math:`y`, consumption is :math:`c`, and :math:`x` are dynamic asset choices.
Function :math:`u` is the current utility given consumption, function :math:`v` is expected future value given
dynamic asset choices, function :math:`g` are the costs of dynamic asset choices to contemporaneous consumptions.
Set :math:`Omega` constrains the asset choice.

Suppose the functions and the constraint set is known, what is the optimal dynamic asset choice that balances the gains
of additional :math:`x` to the future, and the losses of additional :math:`x` to the present.

Single Grid Solution
====================

Nested-Grid Solution
====================

Exact Solution
==============


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
   :nowrap:

    \begin{gather*}
    \max_{ \mathbb{x} \in \Omega}
    u(c)
    +
    v(\mathbb{x})\\
    c = y - g\left(\mathbb{x}\right)
    \end{gather*}

* Income and associated state variables is :math:`y`
* Consumption is :math:`c`
* Dynamic asset choices are :math:`x`
* Function $u$ is the current utility given consumption
* Function :math:`v` is expected future value given dynamic asset choices
* Function :math:`g` are the costs of dynamic asset choices to today c
* Set :math:`\Omega` constrains the asset choice

Suppose the functions and the constraint set is known, what is the optimal
dynamic asset choice that balances the gains of additional :math:`x` to the
future, and the losses of additional :math:`x` to the present.

Discrete Choice
---------------

If the asset choice is discrete in the model, then optimal choices should be
determined over the discrete grid, at all points of the discrete choice set.

Continuous Choice-Level Discretize
-----------------------------------

We want to evaluate both :math:`u` and :math:`v` given the full domain of the
continuous choice, but the number of possible choice points is infinite. Exact
optimal continuous choices generally can not be found, because we do not have
closed-form formulations of solutions for :math:`v`.

We can discretized a continuous grid. It is important to note, however, that if
the model also has discrete asset choices, then discretizing the continuous
assets is conceptually strange. We want to distinguish between the model
discrete choices and choices that are discretized from underlying model
continuous choice variables.

Continuous Choice-Percentage Discretize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One asset discretization method is to reset choices so that they are solved as
percentages.

.. math::
   :nowrap:

    \begin{gather*}
    \max_{ \mathbb{\phi_x} \in [0, \eta, 2\cdot\eta , \cdots, 1 - \eta,  1]}
    u(c)
    +
    v(\mathbb{x})
    \\
    c = h\left(y, \phi_x\right)\cdot\phi_x\\
    x = h\left(y, \phi_x\right)\cdot\left(1-\phi_x\right)
    \end{gather*}

In the re-statement of the problem above:

* Dynamic percentage asset choices are :math:`\phi_x`
* Function :math:`h` is the resource available to divide between $c$ and $a$

Function $h$ is a function of state variables and also the percentage asset
choice :math:`\phi_x` which could have associated costs that change resources
available for consumption and savings/borrowing.

Nested Grid Discretize
----------------------

Another method is to iteratively solve for optimal choices by *zooming-in*.
Solve the discrete optimization problem :math:`j` times, each time over :math:`N` points.
After each iteration, zoom in to the max choice point and generate a denser grid
between the max choice point and the closest surrounding grid points. This could
lead to a significant increase in solution precision without additional
computational burdens. This uses :math:`N \cdot j` number of grid points, and
achieves the same accuracy as if there are :math:`N^{j}` choice grid points.

* :math:`j`, the number of zooming-in iterations
* :math:`J`, the total number of zooming-in iterations
* :math:`n`, one of the :math:`N` grid points per iteration
* :math:`N`, the number of grid points per iteration

This is not a method that will work generally for any kind of optimization
problems. But it works for models with utility functions and income processes
that are normally assumed by dynamic heterogeneous agents models. The method
breaks down potentially if the the max choice grid point picked from the first
iteration is not actually close to true max, but that another point from the
initial choice grid was closer to the true max.

This method could be written down as:

.. math::
   :nowrap:

    \begin{gather*}
    \max_{
      n^{j}
    }
    u(c)
    +
    v(\mathbb{x})
    \\
    n^{j} \in \Omega^{j} \equiv \left\{
    n \in \mathbb{N}
    \colon
    \mid n - n^{\ast,j-1 } \mid
     \le \frac{N^{j}}{2}
    \text{, and, }
    n \in \left\{0, N^{J-j}, 2N^{J-j}, ..., \left(N-1\right)N^{J-j}, N^{J}\right\}
    \right\}
    \\
    c = h\left(y, \frac{n^{j}}{N^{J}}\right)\cdot\frac{n^{j}}{N^{J}}\\
    x = h\left(y, \frac{n^{j}}{N^{J}}\right)\cdot\left(1-\frac{n^{j}}{N^{J}}\right)
    \end{gather*}

Iterative Convergence
---------------------

Various iterative-convergence algorithm that might or might not depend on
objective function derivatives are often used to solve for optimal choices.
These methods are designed to be efficient in the sense of requiring the least
amounts of total computing resources. But they might not be efficient in the
sense of requiring the least amount of time when the researcher has access to
large sets of parallel computing resources. For example, in problems with one
bounded asset choice, bisection is a reliable algorithm.

One potential issue here is step-size for approximating derivatives for
derivative-based methods. Given various approximations, there might be many
local max/min that are not model generated but that are products of
approximation errors.

Using these methods involves a reading the documentations for various existing
minimizers in the `scipy optimization modules
<https://docs.scipy.org/doc/scipy/reference/optimize.html>`__

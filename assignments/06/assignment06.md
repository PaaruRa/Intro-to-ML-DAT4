## Assignment 06

In this assignment, you'll create a class to perform Linear Regression.

### Learning goals

- Learn a bit about what's under the hood in sklearn classes.
- Internalize Linear Regression.

### Background

Linear Regression models an output response i.e a dependent variable (`y`) as linear combination of several
independent variables (`x`s).

Say we have three inputs: $x_{1}$, $x_{2}$ and $x_{3}$.

Then the output is modeled as:

$$
y = \beta_{0} + \beta_{1}x_{1} + \beta_{2}x_{2} + \beta_{3}x_{3}
$$

Training (i.e `fit`ting in sklearn terminology) means finding the values of the $\beta$s to fit the given 
data (of $x$s and $y$s) the best.

Linear regression can be solved analytically with the normal equation:

$$
\beta = (X^{T}X)^{-1}X^{T}y
$$

Where $X$ is a matrix where each row is an instance and each column is a feature.

### The Task

Create a module `linear` that has a class `LinearRegression`.

The class should have a `fit` method that takes training data (`X` and `y`) and 
calculates coefficients internally.

It should also have a `predict` method that accepts inputs (`X`s) and uses the coefficients
to generate and return predictions.

Basically, all of the code in `run.py` (that imports and uses `linear`) should work as expected.

Note: You need to add a column of 1s to the input corresponding to $\beta_{0}$.

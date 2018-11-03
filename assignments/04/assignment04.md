## Assignment 04

In this assignment, you'll create a barebones `pandas` replica.

### Learning goals

- Become familiar with Python classes and enriching them with [dunder methods](https://dbader.org/blog/python-dunder-methods).
- Think about what libraries like pandas do under the hood.

### Background

Most of working with pandas is about working with the `Series` and 
`DataFrame` classes.

`Series` can be thought of an "smart array" while `DataFrame` can, in a way, be thought of as a dictionary of `Series`
objects.

We'll follow that mental model in this assignment.

### The Task

Create a module `danphe` that has two classes `Series` and `DataFrame`.

The `Series` class is basically a list with a name. 
It should support numerical indexing and have a `mean` method that returns the mean of its values.

The `DataFrame` class should be constructed from a dictionary whose values are `Series` objects.
It should support dictionary-like access to its underlying Series dictionary.

Basically, all of the code in `run.py` (that imports and uses `danphe`) should work.

*Hint: You need to define `__getitem__`, and `__str__` dunder methods.*

### Extra

- Have a `shape` property on the DataFrame just like in pandas.
- Also define `__repr__` on the classes. See [difference](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr) between `__str__` and `__repr__`.

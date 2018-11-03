## Assignment 02

In this assignment you'll write a Python module that
has a function to rotate given points.

### Learning goals

- Become comfortable with modular thinking.
- Learn to write modules that can be used in other modules.
- Become familiar with numpy.
- Learn a bit of math i.e become familiar with Matrices as transformations.

### Background

Linear Transformations can be represented by matrices.
Watch [this](https://goo.gl/RFxFNr) for the magic. 

So rotation can be defined by a matrix as well. ( [8:00](https://youtu.be/kYB8IZa5AuE?t=482) of the same video).

With that we can rotate given points by simply multiplying the vector representation of those points by that matrix.

### The task

Complete the `rotate` function in `rotations.py`.

It should accept a 2D numpy array representing list of points and then return the rotations of the points.
The direction to rotate (clockwise or anti-clockwise) should be an argument to the function.

### Notes

- The whole [Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
  playlist by 3Blue1Brown is englightening (and short!). Recommended watch.

### Extra

- Plot the points in `run.py` before and after the rotations.
- Raise an exception if the direction provided isn't valid.

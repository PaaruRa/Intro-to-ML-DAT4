## Assignment 01

In this assignment you'll write a **Python script** to count names that start with a particular letter
and also broken down by gender (male-female).

### Learning goals

- Become familiar with writing Python scripts.
- Become familiar with the `if __name__ == '__main__':` construct.
- Become comfortable with Python's core data structures like Dictionary and list.
- Learn to import and use modules. 

### Background

`genders.csv` contains 8323 names, their gender and count:

|name |gender  |count |
|-----|---------|-------|
|aabha | female | 3|
|aabhas | male | 2|
|aabhash | male | 4|
|aabhesh | male | 2|
|aabhusan | male | 2|
|... | ... | ...|

We want to get a total count for each letter and gender. 
Eg: `count` of `female`s whose name start with `a` is 1000,... etc.

### The Task

Complete the code in `name_count.py`.

When it is run as `python name_count.py`, it should:

1. Read in `genders.csv`. Use the `csv` module.
2. Create a nested dictionary keyed by the letter and gender i.e `name_counts['a']['female']` should give
   the total count of female names that start with `a`.
3. Write the result back to a file `name_counts.csv` with columns `letter`, `gender` and `count`.

|name |gender  |count |
|-----|---------|-------|
|a | female | 1000|
|b | female | 2000|
|... | ... | ...|


Notice the use of `if __name__ == '__main__':` construct to prevent the code from being run when imported in other places.
Refer to [this article](https://www.bogotobogo.com/python/python_if__name__equals__main__.php).

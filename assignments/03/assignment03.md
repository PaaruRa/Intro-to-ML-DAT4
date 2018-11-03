## Assignment 03

In this assignment, you'll do the same task as in Assignment 01 but using `pandas` instead.

### Learning goals

- Become familiar with common data manipulations in pandas
- Compare and contrast the two approaches

### Background

Pandas makes it easy to perform a lot of common data manipulations and analysis.

### The Task

Complete the code in `name_count.py`.

Just as last time, when it is run as `python name_count.py`, it should:

1. Read in `genders.csv`. Use the `csv` module.
2. Find count of names by first letter and gender.
3. Write the result back to a file `name_counts.csv` with columns `letter`, `gender` and `count`.

*Hint: One way would be to use `map` on `name` to get new column `letter` and then `groupby` letter and gender.*

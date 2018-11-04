## Assignment 0

In this assignment, you'll learn to push your work into the repo.

1. Clone this repository locally. 

```
git clone https://github.com/mandalraju/MPercept-Academy-02DSAI
```

2. Create a local branch in the format `{name}/assignment-{num}` from `master`

Eg:

```
git checkout master
git checkout -b bijay/assignment-00 
```

3. Complete your assignment in a folder of your own name. 
It should have a structure same as the `assignments` folder.

So, for this assignment you'll put your solution in `{name}/00/`.

4. Do the assignment.

Assignment 00 is to create a `hello.py` file that prints "Hello World" when run. 
Again, keep the solution i.e `hello.py` in the corresponding folder and obviously
make sure it works. 

5. Add changes and commit.

Eg:

```
git add bijay/assignment-00/hello.py
git commit -m "Add Solution for Assignment 00 (Bijay)"
```

6. Push the branch to the remote repository

Eg:

```
git push origin bijay/assignment-00
```

7. Go to the branch on Github and create a pull request on `master`.

8. Enjoy a cup of tea. 

## Note:

Use `git status` regularly to... well, see the status of the repository.

Also, make heavy use of `git log` and `git diff`!

Pull `master` intermittently to get the latest changes. 

Optional:
You can rebase your branch on master to get the changes into your branch. 

Eg:
```
# Assuming you are on bijay/assignment-00
git rebase master
```

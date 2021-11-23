# Pit: Git, but with Python

(In progress)

Building Git with python for learning purposes.

Based in the book 'Building Git' by James Coglan. 
In the book he uses Ruby to implement his version of Git called 'Jit'.

## Part I. Storing changes. Chapter 3. The first commit

## Todo:
- [x] Chapter 3.1
- [x] Chapter 3.2.1
- [ ] Chapter 3.2.2
- [ ] Chapter 3.2.3

## Runtime:
Python 3.10.0
## OS:
Windows

## If you want to try it:

Clone the repo:

`> git clone git@github.com:benjaminhonorio/pit.git`

Create and activate new python environment:

`> python -m venv pit_env`

`> ./pit_env/Scripts/activate`

Install requirements.txt:

`> pip install -r requirements.txt`

Run it (only works in pit folder at the moment):

`> cd  pit`

`> python pit.py init`

You should see in the console:

`> Initialized empty Pit repository in '<your_path_here>'`

Try commit command (only saves files in pit folder at the moment):

`> python pit.py commit`

After that you should see the files that are been saved to the repository with their respective objects ids. Something like:

```
-blob.py
64810ed3b745450762b28b2ef09d7e2fdb22a64a
-database.py
42546da567cbc50f4b7fb76b8412492b73e0f1dd
-pit.py
1b17871390410c42f7004147fd7c4f624be5002f
-tests.py
4d794c66b9c7ec35a8ce0d9dd20965e78062164e
-workspace.py
9f67807ebb9e76da5fd7af8eb3396a38df18cd7a
```
These will be used later to craft the commit id

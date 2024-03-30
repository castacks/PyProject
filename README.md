
# Practice of Python import.

# Task goal

Fix the this Python project such that one can do the following:
- Run `entry_point.py` of the `model` folder.
- Run `run_test.py` of the `test` folder.

The fix should not change the folder structure, foldernames, and filenames. Modify the content of the files or create necessary files to do the fix.

# One solution

With this branch, the solution allows to run the above two scripts differently.

To run `entry_point.py`. Do

```bash
cd PyProject
python -m model.entry_point
```

To run `run_test.py`. Do

```bash
cd PyProject
python ./test/run_test.py
```

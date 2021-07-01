#DupsRemover
An OS-agnostic program that searches for duplicate files on your machine, presents them to you, and removes them permanently.

###Features
:white_check_mark: Functional and easy to use
:white_check_mark: Automates the hassle of locating and removing duplicated directories and files
:white_check_mark: Neat, colorful, and attractive CLI
:white_check_mark: Works on any operating system

###Future Updates
One important update that will be implemented some time in the near future is that the program will search for duplicates of more multiplicity. Currently, the program only searches for the first iteration of a duplicated file or directory: names that end in (1). Acknowledging that there can also be duplicates of (2), (3), (4), etc., I will work to reflect this reality in the program.

###Fixes
- [x] Fix a bug that crashes the program if a duplicate folder is not empty (OSError Errno 39)
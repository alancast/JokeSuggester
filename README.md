# JokeSuggester
## Repo Rules:
1. ALWAYS PULL BEFORE YOU PUSH. Honestly just use the desktop
    client GUI. We all have Macs and it has a really nice 
    Mac GUI, so use it.
    -Link: https://desktop.github.com/
2. Put any datasets in folder at top of repo titled "Datasets".

    -I have already added to the .gitignore "Datasets/*"
    so that none of these potentially large files get pushed
    to git (as you don't want the repo to grow too large).
3. Before each function comment what parameters it takes 
    as input and what it returns as output. 

    Example (in python):
    ```python
    # INPUTS: training or dev filename
    # RETURNS: target (nparray of ints) and data (list of strings)
    def parse_file(file):
    ```
4. Try to keep lines to <60 characters in case we open file
    in VIM or emacs or something
5. Try not to use namespace std (good career habit to get into)

## Repo structure:
### Directories:
    -Datasets/
        This is a directory that is pretty self explanatory.
        It is comprised of whatever datasets we build
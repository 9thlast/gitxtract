gitxtract is a tool for searching and extracting strings from any and all text that has ever been in a git repository.

# synopsis
```
usage: gitxtract [-h] [-v] {all} ...

extract strings from git repository histories

positional arguments:
  {all}
    all          search for all matches of a regex in the history

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  turn on debug logging
```

# usage
currently, there is only one subcommand: `all` that attempts to open the current directory as a git repository, and takes a single pattern to match. the command first checks if the supplied pattern is in a key-value table of patterns:
* if the pattern is in the pattern list, then it uses the value from the pattern list as the regex to search
* otherwise, it compiles the raw string to regex and searches using that

# issues, questions, and new patterns
if you encounter any problems or have any questions, feel free to create an issue on the [issues page](https://github.com/9thlast/gitxtract/issues). forks and PRs are welcome, especially PRs that include new patterns. to add new patterns, add entries [here](https://github.com/9thlast/gitxtract/blob/main/gitxtract/patterns.py).

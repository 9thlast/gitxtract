import re
import logging
import time
from pygit2 import Repository


logger = logging.getLogger('gitxtract')


def get_git_history(repo):
    history = ''
    head = repo[repo.head.target]
    for commit in repo.walk(repo.head.target):
        diff = repo.diff(commit, head)
        for delta in diff:
            for hunk in delta.hunks:
                for line in hunk.lines:
                    history += line.content
    return history


class GitExtractor:
    def __init__(self):
        logger.debug('initializing GitExtractor in current directory')
        start = time.perf_counter()
        self.repo = Repository('.git')
        self.history = get_git_history(self.repo)
        end = time.perf_counter()
        logger.info(f'calculated history of current repository in {round(end - start, 4)}s')

    def extract(self, regex, compile=True):
        logger.debug(f'searching history for {regex}')
        if compile:
            r = re.compile(regex, re.MULTILINE)
        else:
            r = regex
        matches = re.findall(r, self.history)
        unique = list(set(matches))
        logger.info(f'found {len(unique)} unique matches')
        return unique

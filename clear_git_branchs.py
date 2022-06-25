import git

PATH = './git_python'
REPO = git.Repo.init(PATH)

REPO.git.checkout('master')
for branch in REPO.branches:
    if branch.name != 'master':
        REPO.git.branch('-D', branch)

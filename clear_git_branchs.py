import git

PATH = './git_python'
REPO = git.Repo.init(PATH)

REPO.git.checkout('main')
for branch in REPO.branches:
    if branch.name != 'main':
        REPO.git.branch('-D', branch)

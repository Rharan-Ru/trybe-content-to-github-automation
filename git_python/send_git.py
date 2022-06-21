import git

REPO = git.Repo('/home/monke/sele-learn/git_python')
PATH = './'

try:
    def create_branch_add_files(branch_name, path_dir, index):
        REPO.git.branch(branch_name)
        REPO.git.checkout(branch_name)
        open(f'{path_dir}/exercises.js', 'w').close()
        REPO.git.add('--all')
        REPO.index.commit(f'Exercicios {index}')
        # REPO.git.push('--set-upstream', REPO.remote().name, branch_name)
except Exception:
    REPO.git.checkout('main')
    for branch in REPO.branches:
        if branch.name != 'main':
            REPO.git.branch('-D', branch)
finally:
    REPO.git.checkout('main')
    for branch in REPO.branches:
        if branch.name != 'main':
            REPO.git.branch('-D', branch)

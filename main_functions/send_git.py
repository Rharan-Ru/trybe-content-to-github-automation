import git

PATH = './git_python'
REPO = git.Repo.init(PATH)
REPO.git.add('--all')
REPO.index.commit(f'Init repo')

try:
    def create_branch_add_files(branch_name, path_dir, index):
        REPO.git.branch(branch_name)
        REPO.git.checkout(branch_name)
        open(f'{path_dir}/exercises.js', 'w').close()
        REPO.git.add('--all')
        REPO.index.commit(f'Exercicios {index}')
        # Inicie um repositório git e coloque como origin deste repositório para dar git push, descomente esta linha após isto
        # REPO.git.push('--set-upstream', REPO.remote().name, branch_name)
except Exception:
    REPO.git.checkout('master')
    for branch in REPO.branches:
        if branch.name != 'master':
            REPO.git.branch('-D', branch)

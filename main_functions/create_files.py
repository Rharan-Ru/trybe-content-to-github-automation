import os
from .send_git import create_branch_add_files


REPLACE_CHARS = ['/', ':', ' - ', ' ', ',', '--', '---']


def create_files(parent, child, index):
    if 'projeto' in child.lower():
        return
    parent = replace_characteres(REPLACE_CHARS, parent)
    child = replace_characteres(REPLACE_CHARS, child)
    path = './git_python/'
    parent_path = f'{path}/{parent}'
    child_path = f'{parent_path}/{child}'
    try:
        os.mkdir(parent_path)
        os.mkdir(child_path)
        create_branch_add_files(f'Exercicios/{index}', child_path, index)
        print(f'[ X ]Folder: {child}')
        return child_path
    except OSError as e:
        os.mkdir(child_path)
        create_branch_add_files(f'Exercicios/{index}', child_path, index)
        print(f'[ X ]Folder: {child}')
        return child_path


def replace_characteres(list_char, sentence):
    for char in list_char:
        sentence = sentence.replace(char, '-')
    return sentence.lower()

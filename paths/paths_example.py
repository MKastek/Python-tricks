import pathlib

cwd = pathlib.Path.cwd()
print('current working directory:', cwd)

home = pathlib.Path.home()
print('home directory:', home)

print('joined paths:', cwd.joinpath('data'))

path_to_file = cwd.joinpath('test.md')
text = path_to_file.read_text()
print('text:')
print(text)

# Picking Out Components of a Path
"""
name: the file name without any directory
.parent: the directory containing the file, or the parent directory if path is a directory
.stem: the file name without the suffix
.suffix: the file extension
.anchor: the part of the path before the directories
"""
print('Picking Out Components of a Path')
print(path_to_file)
print('file name:', path_to_file.name)
print('file parent', path_to_file.parent)
print('file name without suffix:', path_to_file.stem)
print('file extension:', path_to_file.suffix)
print('anchorr:', path_to_file.anchor)

# Glob
print(list(cwd.glob('*.md')))
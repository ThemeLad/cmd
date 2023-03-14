import os
import sys


def get_theme_paths() -> list[str]:
    current_dir = os.getcwd()
    args = sys.argv[1:]
    theme_paths = []
    if len(args):
        for theme_path in args:
            full_path = os.path.join(current_dir, theme_path)
            if os.path.isdir(full_path):
                theme_paths.append(full_path)
        return theme_paths
    else:
        files = os.listdir(current_dir)
        for file in files:
            if os.path.isdir(file):
                theme_paths.append(os.path.join(current_dir, file))
        return theme_paths


def get_valid_theme_paths() -> list[str]:
    theme_paths = get_theme_paths()
    valid_theme_paths = []
    for theme_path in theme_paths:
        for file in os.listdir(theme_path):
            file_path = os.path.join(theme_path, file)
            if os.path.isdir(file_path) and file.endswith('-master'):
                valid_theme_paths.append(file_path)
    return valid_theme_paths


if __name__ == '__main__':
    valid_theme_paths = get_valid_theme_paths()
    print(valid_theme_paths)

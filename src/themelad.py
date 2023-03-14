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
        dirs = os.listdir(current_dir)
        for dir in dirs:
            theme_paths.append(os.path.join(current_dir, dir))
        return theme_paths


def get_valid_theme_paths() -> list[str]:
    theme_paths = get_theme_paths()
    valid_theme_paths = []
    for theme_path in theme_paths:
        # Check inside theme_path for master theme dir
        pass
    return valid_theme_paths


if __name__ == '__main__':
    theme_paths = get_valid_theme_paths()

import os
import sys


def get_theme_paths() -> list[str]:
    current_dir = os.getcwd()
    args = sys.argv[1:]
    if len(args):
        theme_paths = []
        for theme_path in args:
            full_path = os.path.join(current_dir, theme_path)
            if os.path.isdir(full_path):
                theme_paths.append(full_path)
        return theme_paths
    else:
        theme_paths = []
        dirs = os.listdir(current_dir)
        for dir in dirs:
            theme_paths.append(os.path.join(current_dir, dir))
        return theme_paths


if __name__ == '__main__':
    theme_paths = get_theme_paths()
    print(theme_paths)

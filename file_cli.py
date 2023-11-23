import os
import datetime
import json
import argparse


def list_directory(path='.'):
    try:
        return os.listdir(path), None
    except Exception as e:
        return None, str(e)


# -----------------------------------------------------

def change_directory(path):
    try:
        os.chdir(path)
        return f"Changed to directory {path}", None
    except Exception as e:
        return None, str(e)

# -----------------------------------------------------


def make_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        return f"Directory created: {path}", None
    except Exception as e:
        return None, str(e)

# -----------------------------------------------------


def remove_directory(path):
    try:
        os.rmdir(path)
        return f"Directory removed: {path}", None
    except Exception as e:
        return None, str(e)

# -----------------------------------------------------


def remove_file(file_path):
    try:
        os.remove(file_path)
        return f"File removed: {file_path}", None
    except Exception as e:
        return None, str(e)

# -----------------------------------------------------


def copy(src, dest):
    try:
        if os.path.isdir(src):
            os.system(f"cp -r {src} {dest}")
        else:
            os.system(f"cp {src} {dest}")
        return f"Copied from {src} to {dest}", None
    except Exception as e:
        return None, str(e)

# -----------------------------------------------------


def move(src, dest):
    try:
        os.rename(src, dest)
        return f"Moved from {src} to {dest}", None
    except Exception as e:
        return None, str(e)

# -----------------------------------------------------


def find_files(start_path, pattern):
    try:
        matches = []
        for root, dirs, files in os.walk(start_path):
            for file in files:
                if pattern in file:
                    matches.append(os.path.join(root, file))
        return matches, None
    except Exception as e:
        return None, str(e)

# -----------------------------------------------------


def cat(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read(), None
    except Exception as e:
        return None, str(e)

# -----------------------------------------------------


def log_command(command, args, outcome, error=None):
    with open("commands.log", "a") as file:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "time": time_now,
            "command": command,
            "arguments": args,
            "outcome": outcome,
            "error": error
        }
        file.write(json.dumps(log_entry) + "\n")

# -----------------------------------------------------


def setup_parser():
    parser = argparse.ArgumentParser(description="File Manipulation CLI")
    subparsers = parser.add_subparsers(
        dest="command", help="Available commands")

    # ls command
    ls_parser = subparsers.add_parser("ls", help="List directory contents")
    ls_parser.add_argument(
        "path", nargs="?", default=".", help="Directory path")

    # cd command
    cd_parser = subparsers.add_parser("cd", help="Change directory")
    cd_parser.add_argument("path", help="Path to change to")

    # mkdir command
    mkdir_parser = subparsers.add_parser(
        "mkdir", help="Create a new directory")
    mkdir_parser.add_argument("path", help="Directory path to create")

    # rmdir command
    rmdir_parser = subparsers.add_parser("rmdir", help="Remove a directory")
    rmdir_parser.add_argument("path", help="Directory path to remove")

    # rm command
    rm_parser = subparsers.add_parser("rm", help="Remove a file")
    rm_parser.add_argument("file_path", help="File path to remove")

    # cp command
    cp_parser = subparsers.add_parser("cp", help="Copy files or directories")
    cp_parser.add_argument("src", help="Source path")
    cp_parser.add_argument("dest", help="Destination path")

    # mv command
    mv_parser = subparsers.add_parser(
        "mv", help="Move files or directories")
    mv_parser.add_argument("src", help="Source path")
    mv_parser.add_argument("dest", help="Destination path")

    # find command
    find_parser = subparsers.add_parser(
        "find", help="Search for files or directories")
    find_parser.add_argument("start_path", help="Directory to start searching")
    find_parser.add_argument("pattern", help="Pattern to search for")

    # cat command
    cat_parser = subparsers.add_parser("cat", help="Display file contents")
    cat_parser.add_argument("file_path", help="File path to display")

    return parser

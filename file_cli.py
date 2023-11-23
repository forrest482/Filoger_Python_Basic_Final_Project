import os


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

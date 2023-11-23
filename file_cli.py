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

import os


def list_directory(path='.'):
    try:
        return os.listdir(path), None
    except Exception as e:
        return None, str(e)

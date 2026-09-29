import os

def mkdir(name: str) -> None:
    try:
        os.mkdir(name)
    except FileExistsError:
        pass
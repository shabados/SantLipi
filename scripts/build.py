from scripts.make import make
from scripts.qa import qa


def main():
    # generate font files
    make()

    # generate qa files
    qa()

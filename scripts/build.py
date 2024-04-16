from scripts.make import main as make
from scripts.qa import main as qa


def main():
    # generate font files
    make()

    # generate qa files
    qa()

from scripts.make import make
from scripts.qa import qa
from scripts.ensure_build_dir import ensure_build_dir


def main():
    ensure_build_dir()

    # generate font files
    make()

    # generate qa files
    qa()

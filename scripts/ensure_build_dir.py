import os


def ensure_build_dir():
    # Ensure build dir exists
    build_dir = "./build"
    if not os.path.exists(build_dir):
        os.mkdir(build_dir)

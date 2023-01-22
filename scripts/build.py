import subprocess


def fontmake():
    cmd = ["fontmake", "-g", "./sources/SantLipi.glyphs"]
    variable_output = ["-o", "variable"]
    subprocess.run(cmd)  # defaults to otf and ttf
    subprocess.run(cmd + variable_output)

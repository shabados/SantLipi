import subprocess
from fontTools.ttLib import TTFont


def fontmake():
    cmd = ["fontmake", "-g", "./sources/SantLipi.glyphs"]
    variable_output = ["-o", "variable"]
    interpolate_instances = ["-i", "-o", "ttf"]
    subprocess.run(cmd)  # defaults to otf and ttf
    subprocess.run(cmd + variable_output)
    subprocess.run(cmd + interpolate_instances)

    variable_font = TTFont("./variable_ttf/SantLipi-VF.ttf")
    variable_font.flavor = "woff2"
    variable_font.save("./variable_ttf/SantLipi-VF.woff2")

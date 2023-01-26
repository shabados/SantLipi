import os
import subprocess
from fontTools.ttLib import TTFont

from scripts.ensure_build_dir import ensure_build_dir


def make():
    # generate instanced and variable ttf fonts
    cmd = [
        "fontmake",
        "-g",
        "./sources/SantLipi.glyphs",
        "--instance-dir",
        "{tmp}",
        "--master-dir",
        "{tmp}",
    ]
    variable_output = ["-o", "variable"]
    interpolate_instances = ["-i", "-o", "ttf"]
    subprocess.run(cmd + variable_output)
    subprocess.run(cmd + interpolate_instances)

    # create woff2 compression of variable ttf font
    variable_font = TTFont("./variable_ttf/SantLipi-VF.ttf")
    variable_font.flavor = "woff2"
    variable_font.save("./variable_ttf/SantLipi-VF.woff2")

    # create woff2 versions of all ttf instances
    input_directory = "./instance_ttf"
    output_directory = "./instance_woff2"
    if not os.path.exists(output_directory):
        # ensure output directory exists
        os.mkdir(output_directory)
    for filename in os.listdir(input_directory):
        file = os.path.join(input_directory, filename)
        new_filename = os.path.splitext(filename)[0] + ".woff2"
        font = TTFont(file)
        font.flavor = "woff2"
        font.save(os.path.join(output_directory, new_filename))

    # move folders to build folder
    ensure_build_dir()
    os.rename(input_directory, os.path.join("./build", "ttf"))
    os.rename(output_directory, os.path.join("./build", "woff2"))
    os.rename("./variable_ttf", os.path.join("./build", "variable"))

import chevron
from scripts.tests import TESTS
import importlib.metadata

site_dir = "build/qa"
template_dir = "scripts/mustache"

VERSION = importlib.metadata.version("santlipi").split(".")
VERSION_STRING = VERSION[0] + "." + VERSION[1].zfill(3)


def create(page, template, hash):
    hash["version"] = VERSION_STRING

    file = open(f"{site_dir}/{page}.html", "w")

    with open(f"{template_dir}/{template}.html", "r") as f:
        file.write(chevron.render(f, hash))

    file.close()


def qa():
    # Instantiate a list of pages for each test in tests.py
    side_by_sides = []
    proof_sheets = []

    # Save each test to the sitemap and create a page for it
    for test in TESTS:
        if test["template"] == "side_by_side":
            side_by_sides.append({"name": test["hash"]["title"], "url": test["url"]})
        if test["template"] == "proof":
            proof_sheets.append({"name": test["hash"]["title"], "url": test["url"]})
        # Create page for test
        create(test["url"], test["template"], test["hash"])

    # Create an index for all tests
    create(
        "index",
        "index",
        {
            "title": "Sant Lipi Test Suite",
            "side_by_side_items": side_by_sides,
            "proof_sheet_items": proof_sheets,
        },
    )

    # Create a README for the build folder
    file = open(f"./build/README.html", "w")

    with open(f"{template_dir}/readme.html", "r") as f:
        file.write(
            chevron.render(
                f,
                {"title": "Readme", "version": VERSION_STRING},
            )
        )

    file.close()

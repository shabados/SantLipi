import importlib.metadata
import os

import chevron

from scripts.tests.tests import tests

# Ensure site dir exists
site_dir = "build/qa/test"
if not os.path.exists(site_dir):
    os.mkdir(site_dir)

template_dir = "scripts/mustache"

VERSION = importlib.metadata.version("santlipi").split(".")
VERSION_STRING = VERSION[0] + "." + VERSION[1].zfill(3)


def create(url, template, hash):
    hash["version"] = VERSION_STRING

    file = open(f"{url}.html", "w")

    with open(f"{template_dir}/{template}.html", "r") as f:
        file.write(chevron.render(f, hash))

    file.close()


def main():
    # Instantiate a list of pages for each test in tests.py
    side_by_sides = []
    proof_sheets = []

    # Save each test to the sitemap and create a page for it
    for test in tests:
        if test["template"] == "side_by_side":
            side_by_sides.append({"name": test["hash"]["title"], "url": test["url"]})
        if test["template"] == "proof":
            proof_sheets.append({"name": test["hash"]["title"], "url": test["url"]})
        # Create page for test
        url = "".join([site_dir, "/", test["url"]])
        create(url, test["template"], test["hash"])

    # Create an index for all tests
    create(
        "build/index",
        "index",
        {
            "title": "Sant Lipi Test Suite",
            "side_by_side_items": side_by_sides,
            "proof_sheet_items": proof_sheets,
        },
    )

    # Create a README for the build folder
    create(
        "build/README",
        "readme",
        {"title": "Readme", "version": VERSION_STRING},
    )

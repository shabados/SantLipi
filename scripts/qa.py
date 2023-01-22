import chevron
from scripts.tests import TESTS

site_root = "qa/html"
template_root = "qa/mustache"


def create(page, template, hash):
    file = open(f"{site_root}/{page}.html", "w")

    with open(f"{template_root}/{template}.html", "r") as f:
        file.write(chevron.render(f, hash))

    file.close()


def generate():
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

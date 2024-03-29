# Contributing

Anyone providing assistance to the future of this project is considered a contributor. Our intention is to signal a safe open-source community. Please help us foster an atmosphere of kindness, cooperation, and understanding. By participating, you agree to abide by the [Contributor Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).

The easiest way to communicate is via [GitHub issues](https://github.com/shabados/SantLipi/issues). Please search for similar issues regarding your concerns before opening a new issue. For everything else we ask to chat about it on [GitHub Discussions](https://github.com/orgs/shabados/discussions) or [Slack](https://chat.shabados.com/).

If you wish to share changes back upstream, please see "[Open Pull Requests](#open-pull-requests)" below.

**Requirements**

- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)

## Run QA (Quality Assurance)

If you simply want to run QA against the latest release of Sant Lipi, then please use the online [Sant Lipi Test Suite](https://shabados.github.io/SantLipi). If you wish to run QA locally:

- Install project dependencies with `poetry install`.
- Build files with `poetry run build`.
- Open `build/index.html` to view the Sant Lipi Test Suite.

## Add QA Tests

- Install project dependencies with `poetry install`.
- Build fonts and QA files with `poetry run build`.
- Edit `scripts/tests.py`.
- Regenerate QA files with `poetry run qa`.
- Open `build/index.html` to confirm.

## Modify/Change Font

- Use [Glyphs 3](https://glyphsapp.com/) to open `sources/SantLipi.glyphs`.
- Run QA locally to confirm changes (see above).

## Open Pull Requests

_Role: contributors wishing to change the project source code_

- Fork this repository
- Create a branch from `main`
- Make any changes
- Submit a pull request

Note: Before creating new branches, ensuring that the forked `main` is up to date with the upstream/original `main` will ease workflow.

## Merge PRs

_Role: project authors/maintainers_

- Pull requests should be squashed or rebased.
- Commit messages on `main` branch should generally conform to [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).
- No commit's type should be `fix`.

**Note**

OpenType specifications only allow for a "Major" and "Minor" version. There is no "Patch" version number. In Sant Lipi packages, the patch number should always be 0. The minor version in Glyphs should be 3 digits long (e.g. SemVer 0.1.0 becomes Version 0.001, SemVer 2.15.0 becomes Version 2.015). Minor version should not exceed 999. If that ever happens, then should probably just bump the Major version number and reset Minor to 0. Installation software can use these version strings to compare font versions. Please adhere to these rules.

**Types**

Some _types_ correlate with incrementing major, minor, and patch versions in [Semantic Versioning](https://semver.org/). These _types_ should only be used for code changes in the `sources` folder. (This folder is considered the project's API.)

- `BREAK` increments major. To be used when making incompatible changes to the API. E.g. deleting glyphs from the font.
- `feat` increments minor. To be used when adding backwards-compatible functionality to the API. E.g. changing metrics, shapes, features, etc.

Project authors/maintainers should never merge a PR whose commit(s) begin with `fix`, as there are no patch bumps for this project. See **Note** above.

All other _types_ are ignored by the version bump workflow. These types are typically used outside the API folder, but may change API source code without actually affecting anything for the end user. Valid non-versioning (non-API related) _types_ include: `build`, `ci`, `docs`, `perf`, `refactor`, `revert`, `style`, and `test`.

## Release

_Role: project authors/maintainers_

See [actions](https://github.com/shabados/SantLipi/actions) for workflows related to bumping version numbers, releasing to GitHub, and publishing packages.

Note: The entire release process can be completed on GitHub in a web browser.

**1. Bump (Version Increment)**

- This workflow bumps/increments the version via a Pull Request.
- The PR will list all the commit history from after the last release.
- It is a good idea to modify the `CHANGELOG.md` in the PR.
- The PR needs to be merged prior to publishing.

Note: Leave the override field blank for automatic versioning. If the PR that is opened bumps incorrectly, it is always possible to close the automatic PR and manually bump a new workflow.

Note: If manually overriding the version bump, remember to use 0 for the patch version number.

**2. Release**

- This workflow should immediately follow a version increment/bump PR merge.
- This workflow will create a GitHub release.
- The tag and title of the release will say "prerelease" on purpose.

**3. Publish**

- This workflow is automatically triggered when pushing a git tag to the repo. A GH action is not able to trigger these conditions; Git tags must be pushed by an admin/user with write permissions.
- Edit the latest release. At the top left click the "tag" dropdown. Create a new tag by omitting `-prerelease`.
- Finish by submitting the form "Update release". This will automatically trigger the publish workflow.
- Optionally go to [tags](https://github.com/shabados/SantLipi/tags) and delete the prerelease tag, which should only have a zip/tar.gz associated with it.

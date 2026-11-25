# decisis demo: Bookshop

A small, made-up Bookshop app that shows [decisis](https://github.com/Vinculums/decisis) at work.

- `docs/adr/` holds the team's decisions. Each ADR carries a rule decisis can check:
  the user interface never imports the database layer, payment changes need a payments review,
  no HIGH advisories in shipped dependencies (with one waiver that expires soon), and GitHub Actions are pinned to a commit.
- `.github/workflows/decisis.yml` runs the decisis Action on every pull request: it comments with the decisions the
  change touches and the rules it breaks, fails the check on a violation, and uploads SARIF to code scanning.

Everything here is synthetic. Open the pull requests to see decisis comment on them.

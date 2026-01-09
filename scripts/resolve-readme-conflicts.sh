#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: resolve-readme-conflicts.sh [--base <branch>] [--archive-dir <dir>]

Resolves README.md conflicts by keeping the mainline README and archiving the
current branch README snapshot under readmes/.

Options:
  --base <branch>       Base branch to take README from (default: origin/main)
  --archive-dir <dir>   Directory for README snapshots (default: readmes)
USAGE
}

BASE_BRANCH="origin/main"
ARCHIVE_DIR="readmes"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --base)
      BASE_BRANCH="$2"
      shift 2
      ;;
    --archive-dir)
      ARCHIVE_DIR="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

git rev-parse --is-inside-work-tree >/dev/null 2>&1 || {
  echo "Not inside a git repository" >&2
  exit 1
}

if ! git ls-files -u -- README.md >/dev/null 2>&1; then
  echo "No conflict detected for README.md" >&2
  exit 0
fi

branch_name=$(git rev-parse --abbrev-ref HEAD)
commit_sha=$(git rev-parse --short HEAD)

mkdir -p "$ARCHIVE_DIR"
archive_file="$ARCHIVE_DIR/README-${commit_sha}-${branch_name//\//-}.md"

if git show ":2:README.md" >/dev/null 2>&1; then
  git show ":2:README.md" > "$archive_file"
else
  git show HEAD:README.md > "$archive_file"
fi

if git show "$BASE_BRANCH":README.md >/dev/null 2>&1; then
  git show "$BASE_BRANCH":README.md > README.md
else
  echo "Base branch README not found: $BASE_BRANCH" >&2
  exit 1
fi

git add README.md "$archive_file"

echo "Archived current README to $archive_file and restored README from $BASE_BRANCH"

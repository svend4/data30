#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: merge-branch.sh <branch> [--base <branch>]

Merges a branch with origin/main, auto-resolves README conflicts via
scripts/resolve-readme-conflicts.sh, and reports any remaining conflicts.

Options:
  --base <branch>   Base branch to merge from (default: origin/main)
USAGE
}

if [[ $# -lt 1 ]]; then
  usage
  exit 1
fi

BRANCH="$1"
shift

BASE_BRANCH="origin/main"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --base)
      BASE_BRANCH="$2"
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

git fetch origin

if ! git show-ref --verify --quiet "refs/heads/$BRANCH"; then
  git checkout -b "$BRANCH" "origin/$BRANCH"
else
  git checkout "$BRANCH"
fi

git merge "$BASE_BRANCH" || true

if git ls-files -u -- README.md >/dev/null 2>&1; then
  scripts/resolve-readme-conflicts.sh --base "$BASE_BRANCH" --archive-dir readmes
fi

if git ls-files -u >/dev/null 2>&1; then
  echo "Conflicts remain. Review with: git status" >&2
  exit 2
fi

echo "Merge completed without remaining conflicts."

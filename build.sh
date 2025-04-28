#!/usr/bin/env bash
# build.sh: automate building source and wheel distributions

set -euo pipefail

# Clean and prepare the release directory
rm -rf release

echo "Building source and wheel distributions..."
python -m build --sdist --wheel --outdir release

echo "Build complete. Distributions in release/:"
ls -l release
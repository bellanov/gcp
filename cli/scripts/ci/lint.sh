#!/bin/bash
#
# Lint Code Base.

set -e

echo "Linting code base..."

# stop the build if there are Python syntax errors or undefined names
flake8 cli --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
flake8 cli --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
# Check for code formatting issues
black --check --target-version py314 cli
isort --check cli

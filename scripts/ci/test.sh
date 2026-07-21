#!/bin/bash
#
# Execute unit tests.

TEST_TYPE=${1:-"unit"}

set -e

echo "Executing Unit Tests..."
coverage run -m pytest -m "$TEST_TYPE" tests/ 

echo "Generating Report..."
coverage report -m

echo "Build HTML Report..."
coverage html

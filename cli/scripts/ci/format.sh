#!/bin/bash
#
# Format Code Base.

echo "Formatting imports..."
isort cli
isort tests

echo "Formatting code base..."
black --target-version py314 cli 
black --target-version py314 tests

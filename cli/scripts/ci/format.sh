#!/bin/bash
#
# Format Code Base.

echo "Formatting imports..."
isort cli

echo "Formatting code base..."
black --target-version py314 cli 

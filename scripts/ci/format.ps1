#!/bin/bash
#
# Format Code Base.

echo "Formatting imports..."
isort gcp
isort tests

echo "Formatting code base..."
black gcp
black tests
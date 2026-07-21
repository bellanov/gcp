#!/usr/bin/env pwsh
#
# Execute unit tests.

param(
    [string]$TestType = "unit"
)

$ErrorActionPreference = "Stop"

Write-Host "Executing Unit Tests..."
coverage run -m pytest -m "$TestType" tests/

Write-Host "Generating Report..."
coverage report -m

Write-Host "Build HTML Report..."
coverage html

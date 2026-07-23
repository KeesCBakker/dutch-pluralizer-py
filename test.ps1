$ErrorActionPreference = "Stop"
$projectRoot = $PSScriptRoot

Write-Host "Building dev container..." -ForegroundColor Yellow
docker build -t dutch-pluralizer-dev -f "$projectRoot/.devcontainer/Dockerfile" "$projectRoot"

Write-Host "Running tests..." -ForegroundColor Yellow
docker run --rm dutch-pluralizer-dev python -m pytest @args

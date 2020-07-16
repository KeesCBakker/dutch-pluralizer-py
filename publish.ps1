$ErrorActionPreference = "Stop"

$env:PIPENV_VERBOSITY = '-1';
git config --global core.safecrlf false

Write-Host ""
Write-Host "Cleaning up..." -ForeGroundColor Yellow
Remove-Item build -Recurse -ErrorAction Ignore
Remove-Item dist -Recurse -ErrorAction Ignore

Write-Host ""
Write-Host "Checking Git status..." -ForeGroundColor Yellow
if(git status --porcelain | where {$_ -match '^\?\?'}){
    Write-Host "DIRTY: Untracked files exist. Add and commit them first."
    Write-Host ""
    exit $LASTEXITCODE
} 
elseif(git status --porcelain | where {$_ -notmatch '^\?\?'}) {
    Write-Host "DIRTY: Uncommitted files exist. Commit them first."
    Write-Host ""
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Installing (Dev) packages..." -ForeGroundColor Yellow
pipenv sync --dev
if($LASTEXITCODE -gt 0){
    Write-Host "Intalling packages failed..." -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Testing..." -ForeGroundColor Yellow
python -m pytest
if($LASTEXITCODE -gt 0){
    Write-Host "Testing failed..." -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Patch version..." -ForeGroundColor Yellow
bumpversion patch

Write-Host ""
Write-Host "Build..." -ForeGroundColor Yellow
python setup.py sdist bdist_wheel
twine check dist/*

Write-Host ""
Write-Host "Distribute..." -ForeGroundColor Yellow
twine upload dist/*
if($LASTEXITCODE -gt 0){
    Write-Host "Distribution failed..." -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Done" -ForeGroundColor Green
Write-Host ""
Write-Host ""

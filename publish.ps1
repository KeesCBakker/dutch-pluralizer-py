$ErrorActionPreference = "Stop"

Write-Host "Cleaning up..." -ForeGroundColor Yellow
Remove-Item build -Recurse -ErrorAction Ignore
Remove-Item dist -Recurse -ErrorAction Ignore

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

Write-Host "Installing (Dev) packages..." -ForeGroundColor Yellow
pipenv sync --dev

Write-Host "Testing..." -ForeGroundColor Yellow
python -m pytest

Write-Host "Patch version..." -ForeGroundColor Yellow
bumpversion patch

Write-Host "Build..." -ForeGroundColor Yellow
python setup.py sdist bdist_wheel
twine check dist/*

Write-Host "Distribute..." -ForeGroundColor Yellow
twine upload dist/*

Write-Host "Done" -ForeGroundColor Green

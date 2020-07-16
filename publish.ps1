$ErrorActionPreference = "Stop"

$env:PIPENV_VERBOSITY = '-1'; 

Write-Output ""
Write-Output "Cleaning up..." -ForeGroundColor Yellow
Remove-Item build -Recurse -ErrorAction Ignore
Remove-Item dist -Recurse -ErrorAction Ignore

Write-Output ""
Write-Output "Checking Git status..." -ForeGroundColor Yellow
if(git status --porcelain | where {$_ -match '^\?\?'}){
    Write-Output "DIRTY: Untracked files exist. Add and commit them first."
    Write-Output ""
    exit $LASTEXITCODE
} 
elseif(git status --porcelain | where {$_ -notmatch '^\?\?'}) {
    Write-Output "DIRTY: Uncommitted files exist. Commit them first."
    Write-Output ""
    exit $LASTEXITCODE
}

Write-Output ""
Write-Output "Installing (Dev) packages..." -ForeGroundColor Yellow
pipenv sync --dev

Write-Output ""
Write-Output "Testing..." -ForeGroundColor Yellow
python -m pytest
Write-Output $LASTEXITCODE

Write-Output ""
Write-Output "Patch version..." -ForeGroundColor Yellow
bumpversion patch

Write-Output ""
Write-Output "Build..." -ForeGroundColor Yellow
python setup.py sdist bdist_wheel
twine check dist/*

Write-Output ""
Write-Output "Distribute..." -ForeGroundColor Yellow
twine upload dist/*

Write-Output ""
Write-Output "Done" -ForeGroundColor Green

$ErrorActionPreference = "Stop"

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

python -m pytest
bumpversion patch
rm dist/*
python setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*
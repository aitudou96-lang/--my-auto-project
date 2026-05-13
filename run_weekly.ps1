$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot
$pythonExe = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $pythonExe)) {
    Write-Error "Python interpreter not found: $pythonExe"
}
& $pythonExe "src\workflows\weekly_review_generator.py"
exit $LASTEXITCODE

@echo off
setlocal
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0run_weekly.ps1"
exit /b %ERRORLEVEL%

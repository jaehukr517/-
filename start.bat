@echo off
setlocal
cd /d "%~dp0"

echo [INFO] Starting 3D baseball game server...
where py >nul 2>nul
if %ERRORLEVEL%==0 (
  py run_game.py
  goto :eof
)

where python >nul 2>nul
if %ERRORLEVEL%==0 (
  python run_game.py
  goto :eof
)

echo [ERROR] Python not found. Please install Python 3 and try again.
echo         https://www.python.org/downloads/windows/
pause

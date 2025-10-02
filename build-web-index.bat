@echo off
setlocal

echo Browser Version HTML Builder
echo ================================================

:: Python version check
python --version >nul 2>&1 || (
  echo [ERROR] Python is not installed.
  echo Please install Python 3.6 or higher.
  echo.
  pause
  exit /b 1
)

:: Execute Python script
echo [RUNNING] Generating index.html...
python tools\build_web_index.py

:: Check result
if %ERRORLEVEL% EQU 0 (
  echo.
  echo [SUCCESS] index.html generated successfully!
  echo File: index.html
  echo Open in browser to use the converter.
) else (
  echo.
  echo [ERROR] HTML generation failed with exit code: %ERRORLEVEL%
  echo Please check:
  echo   - config\mapping.json file exists
  echo   - config\template_columns.json file exists
  echo   - tools\build_web_index.py file exists
)

echo.
echo Press any key to close...
pause >nul

endlocal
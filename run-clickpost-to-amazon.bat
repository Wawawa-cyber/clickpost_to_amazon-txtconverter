@echo off
setlocal

echo Clickpost CSV to Amazon Shipping Confirmation Converter
echo =======================================================

:: Python version check
python --version >nul 2>&1 || (
  echo [ERROR] Python is not installed.
  echo Please install Python 3.6 or higher.
  echo.
  pause
  exit /b 1
)

:: Execute Python script
echo [RUNNING] Starting conversion process...
python tools\clickpost_to_amazon.py %*

:: Check result
if %ERRORLEVEL% EQU 0 (
  echo.
  echo [SUCCESS] Conversion completed successfully!
  echo Check output folder for generated files
) else (
  echo.
  echo [ERROR] Conversion failed with exit code: %ERRORLEVEL%
  echo Please check:
  echo   - CSV file exists in input/ folder and has proper encoding
  echo   - config\mapping.json settings are correct
  echo   - config\config.json settings are correct
)

echo.

echo Press any key to close...
pause >nul

endlocal

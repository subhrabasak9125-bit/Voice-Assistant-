@echo off
REM ============================================================
REM DISHA Enhanced - Launcher Script
REM ============================================================

title DISHA Enhanced - AI Assistant

echo.
echo ============================================================
echo   DISHA Enhanced - JARVIS-like AI Assistant
echo ============================================================
echo.
echo   Initializing systems...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if dependencies are installed
echo Checking dependencies...
python -c "import speech_recognition" >nul 2>&1
if errorlevel 1 (
    echo Installing required dependencies...
    pip install -r requirements_enhanced.txt
    echo.
)

REM Clear screen for clean startup
cls

REM Run DISHA Enhanced
echo Starting DISHA Enhanced...
echo.
python main_enhanced.py

REM Cleanup
if errorlevel 1 (
    echo.
    echo [ERROR] DISHA encountered an error
    pause
)

deactivate

@echo off
rem ============================================================
rem  DISHA — Digital Intelligent System for Human Assistant
rem  Double-click this file to launch DISHA.
rem ============================================================

cd /d "%~dp0"

rem Check if Python is available
python --version >NUL 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Download Python from: https://www.python.org/downloads/
    echo Make sure you tick "Add Python to PATH" during install.
    pause
    exit /b 1
)

rem Install dependencies silently if needed
python -c "import speech_recognition" >NUL 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies.
        pause
        exit /b 1
    )
)

rem Launch DISHA
python main.py

pause

@echo off
setlocal

echo ========================================
echo Text-to-Speech Batch Conversion
echo ========================================

echo.
echo [1/3] Processing: Unit 2 Humanities Reading 1.txt
call python .\text_to_speech.py "Unit 2 Humanities Reading 1.txt"
if %errorlevel% neq 0 (
    echo [ERROR] Failed to process Unit 2 Humanities Reading 1.txt
) else (
    echo [SUCCESS] Completed Unit 2 Humanities Reading 1.txt
)
echo.

echo [2/3] Processing: Unit 2 Humanities Reading 2.txt
call python .\text_to_speech.py "Unit 2 Humanities Reading 2.txt"
if %errorlevel% neq 0 (
    echo [ERROR] Failed to process Unit 2 Humanities Reading 2.txt
) else (
    echo [SUCCESS] Completed Unit 2 Humanities Reading 2.txt
)
echo.

echo [3/3] Processing: Unit 2 Humanities Reading 3.txt
call python .\text_to_speech.py "Unit 2 Humanities Reading 3.txt"
if %errorlevel% neq 0 (
    echo [ERROR] Failed to process Unit 2 Humanities Reading 3.txt
) else (
    echo [SUCCESS] Completed Unit 2 Humanities Reading 3.txt
)
echo.

echo ========================================
echo All conversions completed!
echo ========================================
pause
endlocal

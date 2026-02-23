@echo off
cd /d "%~dp0"

echo [1/3] Copying item_browser.html to src-tauri\frontend\index.html ...
if not exist src-tauri\frontend mkdir src-tauri\frontend
copy /y item_browser.html src-tauri\frontend\index.html >nul
if errorlevel 1 (
    echo ERROR: Failed to copy item_browser.html
    pause & exit /b 1
)

echo [2/3] Building with cargo tauri build ...
set CI=
cargo tauri build
if errorlevel 1 (
    echo ERROR: Build failed
    pause & exit /b 1
)

echo.
echo [3/3] Copying portable exe to project root ...
copy /y src-tauri\target\release\item-browser.exe ItemBrowser.exe >nul
echo.
echo Done!
echo   Portable exe : %~dp0ItemBrowser.exe
echo   Installer    : src-tauri\target\release\bundle\nsis\ItemBrowser_0.1.0_x64-setup.exe

pause

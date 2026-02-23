@echo off
cd /d "%~dp0"
start http://localhost:8765/
python serve_item_browser.py
pause

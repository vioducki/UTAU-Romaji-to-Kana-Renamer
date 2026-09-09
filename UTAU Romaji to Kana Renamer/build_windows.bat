@echo off
python -m pip install pyinstaller
pyinstaller --onefile --windowed --icon=icon.ico --add-data "icon.ico;." --name UTAU-Romaji-to-Kana-Renamer renamer.py
pause

# UTAU Romaji to Kana Renamer

A small Windows Tkinter application that previews and batch-renames `.wav` files from romaji filenames to hiragana/kana filenames.

Place your application icon in this folder as `icon.ico`. The icon should be an ICO file; PNG or JPG files need to be converted first.

## Features

- Select a folder containing `.wav` files.
- Preview the original names and proposed kana names side by side.
- Batch rename the files.
- Undo the most recent batch rename while the app is still open.
- Uses only Python's standard library for the application itself.

## Run from Python

1. Install Python 3.10 or newer from <https://www.python.org/downloads/>.
2. During installation, enable **Add Python to PATH**.
3. Open PowerShell in this project folder.
4. Run:

```powershell
python renamer.py
```

Tkinter is included with the standard Windows Python installer.

## Build a Windows executable

To make an `.exe` that can run without opening Python:

```powershell
python -m pip install pyinstaller
pyinstaller --onefile --windowed --icon=icon.ico --add-data "icon.ico;." --name UTAU-Romaji-to-Kana-Renamer renamer.py
```

The finished executable will be placed in the `dist` folder.

You can also run `build_windows.bat` after installing PyInstaller.

## Publish on GitHub

1. Install [Git for Windows](https://git-scm.com/download/win) or [GitHub Desktop](https://desktop.github.com/).
2. Create a new empty repository on GitHub.
3. In PowerShell, open this project folder and run:

```powershell
git init
git add renamer.py README.md .gitignore build_windows.bat
git commit -m "Initial release"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your repository's URL. Do not commit personal folders, audio files, passwords, or generated build folders.

## Important note about Undo

Undo remembers the most recent rename operation only while the application remains open. It does not store a permanent undo history after the program closes.

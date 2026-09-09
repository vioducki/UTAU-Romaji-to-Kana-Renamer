# UTAU Romaji to Kana Renamer

A small Windows application that previews and batch-renames `.wav` files from romaji filenames to hiragana/kana filenames! For people who are lazy like me!
But now you don't have to manually rename all of your files one by one.
I've only tried this with CV voicebanks but if you'd like to try this with VCV or CVVC then go ahead and you can contact me on Instagram @vioducki.art if it works or not.

## Features

- Pick a folder containing `.wav` files.
- Preview the original names and proposed kana names side by side before actually renaming them
- Batch rename the files so you won't have to do it one by one
- Undo the most recent batch rename while the app is still open in case you want to keep the romaji instead
- Uses only Python's standard library for the application itself (because I kinda only know python and a little bit of html)

## Run from Python
Yeah apparently you don't need to install Python! I thought you did but nope, everything is all packaged up! All you need to do is install the zip file in the Releases, unzip the file and open the `dist` folder and run the exe! Easy as pie! Wait, Pie reference?!?!?!!? PAItomo?!!

## About Undo

Undo remembers the most recent rename only while the app stays open. It doesn't store a permanent undo history after the program closes, so... yeah, be sure you're 100% sure you want to keep the changes before closing the app.

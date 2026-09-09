import os
import re
import sys
import tkinter as tk
from tkinter import filedialog, messagebox


PINK = "#ffa6d4"
GREEN = "#85ff97"
rename_history = []


def resource_path(file_name):
    bundle_folder = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(bundle_folder, file_name)

romaji_to_kana = {
    # basic vowels
    "a": "あ",
    "i": "い",
    "u": "う",
    "e": "え",
    "o": "お",

    # k row
    "ka": "か",
    "ki": "き",
    "ku": "く",
    "ke": "け",
    "ko": "こ",
    "kya": "きゃ",
    "kyu": "きゅ",
    "kyo": "きょ",

    # s row
    "sa": "さ",
    "shi": "し",
    "su": "す",
    "se": "せ",
    "so": "そ",
    "sha": "しゃ",
    "shu": "しゅ",
    "sho": "しょ",

    # t row
    "ta": "た",
    "chi": "ち",
    "tsu": "つ",
    "te": "て",
    "to": "と",
    "cha": "ちゃ",
    "chu": "ちゅ",
    "cho": "ちょ",
    "che": "ちぇ",

    # n row
    "na": "な",
    "ni": "に",
    "nu": "ぬ",
    "ne": "ね",
    "no": "の",
    "nya": "にゃ",
    "nyu": "にゅ",
    "nyo": "にょ",
    "nye": "にぇ",

    # h row
    "ha": "は",
    "hi": "ひ",
    "fu": "ふ",
    "hu": "ふ",
    "he": "へ",
    "ho": "ほ",
    "hya": "ひゃ",
    "hyu": "ひゅ",
    "hyo": "ひょ",
    "hye": "ひぇ",

    # m row
    "ma": "ま",
    "mi": "み",
    "mu": "む",
    "me": "め",
    "mo": "も",
    "mya": "みゃ",
    "myu": "みゅ",
    "myo": "みょ",
    "mye": "みぇ",

    # y row
    "ya": "や",
    "yu": "ゆ",
    "yo": "よ",
    "ye": "いぇ",

    # r row
    "ra": "ら",
    "ri": "り",
    "ru": "る",
    "re": "れ",
    "ro": "ろ",
    "rya": "りゃ",
    "ryu": "りゅ",
    "ryo": "りょ",
    "rye": "りぇ",

    # w row and also n
    "wa": "わ",
    "wo": "を",
    "n": "ん",

    # g row
    "ga": "が",
    "gi": "ぎ",
    "gu": "ぐ",
    "ge": "げ",
    "go": "ご",
    "gya": "ぎゃ",
    "gyu": "ぎゅ",
    "gyo": "ぎょ",

    # z row
    "za": "ざ",
    "ji": "じ",
    "zu": "ず",
    "ze": "ぜ",
    "zo": "ぞ",
    "ja": "じゃ",
    "ju": "じゅ",
    "jo": "じょ",

    # d row
    "da": "だ",
    "di": "ぢ",
    "du": "づ",
    "de": "で",
    "do": "ど",

    # b row
    "ba": "ば",
    "bi": "び",
    "bu": "ぶ",
    "be": "べ",
    "bo": "ぼ",
    "bya": "びゃ",
    "byu": "びゅ",
    "byo": "びょ",

    # p row
    "pa": "ぱ",
    "pi": "ぴ",
    "pu": "ぷ",
    "pe": "ぺ",
    "po": "ぽ",
    "pya": "ぴゃ",
    "pyu": "ぴゅ",
    "pyo": "ぴょ",

    # other
    "fa": "ふぁ",
    "fi": "ふぃ",
    "fe": "ふぇ",
    "fo": "ふぉ",
    "kwa": "くぁ",
    "kwi": "くぃ",
    "kwe": "くぇ",
    "kwo": "くぉ",
    "gwa": "ぐぁ",
    "gwi": "ぐぃ",
    "gwe": "ぐぇ",
    "gwo": "ぐぉ",
    "wi": "ゐ",
    "we": "ゑ",
    "va": "ゔぁ",
    "vi": "ゔぃ",
    "vu": "ゔ",
    "ve": "ゔぇ",
    "vo": "ゔぉ",
}


def list_files_in_folder(folder_path):
    if not folder_path:
        return []

    files = []
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        if os.path.isfile(full_path) and item.lower().endswith(".wav"):
            files.append(item)
    return sorted(files)


def romaji_to_kana_name(name):
    base_name = os.path.splitext(name)[0]
    base_name = base_name.lower()
    base_name = re.sub(r"[^a-z]", "", base_name)

    if not base_name:
        return None

    kana = []
    i = 0
    while i < len(base_name):
        match = None
        longest = ""
        for key in sorted(romaji_to_kana.keys(), key=len, reverse=True):
            if base_name.startswith(key, i):
                if len(key) > len(longest):
                    longest = key
                    match = romaji_to_kana[key]
        if match is None:
            return None
        kana.append(match)
        i += len(longest)

    return "".join(kana)


def rename_batch_files(folder_path):
    files = list_files_in_folder(folder_path)
    renamed = 0
    skipped = 0
    batch_history = []

    for file_name in files:
        new_name = romaji_to_kana_name(file_name)
        if new_name is None:
            skipped += 1
            continue

        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name + ".wav")

        if os.path.exists(new_path):
            base = 1
            while os.path.exists(os.path.join(folder_path, f"{new_name}_{base}.wav")):
                base += 1
            new_path = os.path.join(folder_path, f"{new_name}_{base}.wav")

        os.rename(old_path, new_path)
        batch_history.append((old_path, new_path))
        renamed += 1

    return renamed, skipped, batch_history


def refresh_preview(folder_path):
    before_files = list_files_in_folder(folder_path)
    before_listbox.delete(0, tk.END)
    after_listbox.delete(0, tk.END)

    for file_name in before_files:
        before_listbox.insert(tk.END, file_name)

        converted = romaji_to_kana_name(file_name)
        if converted:
            after_listbox.insert(tk.END, converted + ".wav")
        else:
            after_listbox.insert(tk.END, "-")


def select_folder():
    global rename_history
    folder_path = filedialog.askdirectory(title="Select UTAU voicebank folder!")
    if not folder_path:
        status_var.set("No folder selected.")
        return

    files = list_files_in_folder(folder_path)
    before_listbox.delete(0, tk.END)
    after_listbox.delete(0, tk.END)

    if not files:
        status_var.set(f"Selected folder: {folder_path} (no .wav files found)")
        messagebox.showinfo("No WAV files found!", "This folder doesn't have any .wav files.")
        return

    current_folder.set(folder_path)
    rename_history = []
    refresh_preview(folder_path)
    status_var.set(f"Selected folder: {folder_path}  |  {len(files)} WAV file(s)")


def batch_rename():
    global rename_history
    folder_path = current_folder.get()
    if not folder_path:
        messagebox.showwarning("Hold up!", "Please select a folder first.")
        return

    renamed, skipped, batch_history = rename_batch_files(folder_path)
    rename_history = batch_history

    refresh_preview(folder_path)
    status_var.set(f"Renamed {renamed} file(s). Skipped {skipped} unrecognized file(s).")
    messagebox.showinfo("Batch rename complete!", f"Renamed {renamed} file(s). Skipped {skipped} file(s).")


def undo_rename():
    global rename_history
    if not rename_history:
        messagebox.showinfo("Nothing to undo...", "There are no recent renames to restore.")
        return

    folder_path = current_folder.get()
    if not folder_path:
        messagebox.showwarning("Hold up!", "Please select a folder first.")
        return

    for old_path, new_path in reversed(rename_history):
        if os.path.exists(new_path):
            os.rename(new_path, old_path)

    rename_history = []
    refresh_preview(folder_path)
    status_var.set(f"Undid rename for {folder_path}.")
    messagebox.showinfo("Undo complete!", "The WAV files were restored to their original names.")


root = tk.Tk()
root.title("Romaji to Kana Renamer")
root.geometry("760x520")
root.configure(bg=GREEN)

icon_path = resource_path("icon.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

current_folder = tk.StringVar(value="")
status_var = tk.StringVar(value="Select a folder to begin!")

header = tk.Label(root, text="Romaji to Kana Renamer", font=("Segoe UI", 12, "bold"), bg=GREEN)
header.pack(pady=(16, 8))

subheader = tk.Label(root, text="Batch rename CV UTAU voicebank .wav files from romaji to kana!", font=("Segoe UI", 10), bg=GREEN)
subheader.pack(pady=(0, 16))

subheader = tk.Label(root, text="(Created by vioducki)", font=("Segoe UI", 8, "italic"), bg=GREEN)
subheader.pack(pady=(0, 16))

button_frame = tk.Frame(root, bg=GREEN)
button_frame.pack(pady=8)

button_style = {
    "bg": PINK,
    "fg": "black",
    "activebackground": "#ffbfdc",
    "activeforeground": "black",
    "relief": "ridge",
    "bd": 2,
    "padx": 18,
    "pady": 8,
    "font": ("Segoe UI", 10, "bold"),
    "highlightbackground": "#d87cae",
    "highlightthickness": 1,
    "borderwidth": 2,
    "cursor": "hand2",
}

button = tk.Button(button_frame, text="Choose Folder", command=select_folder, **button_style)
button.pack(side=tk.LEFT, padx=8)
button.config(
    compound="left",
    padx=18,
    pady=8,
    relief="raised",
    borderwidth=2,
    highlightbackground="#d87cae",
    highlightthickness=1,
)

rename_button = tk.Button(button_frame, text="Rename Files", command=batch_rename, **button_style)
rename_button.pack(side=tk.LEFT, padx=8)
rename_button.config(
    compound="left",
    padx=18,
    pady=8,
    relief="raised",
    borderwidth=2,
    highlightbackground="#d87cae",
    highlightthickness=1,
)

undo_button = tk.Button(button_frame, text="Undo Rename", command=undo_rename, **button_style)
undo_button.pack(side=tk.LEFT, padx=8)
undo_button.config(
    compound="left",
    padx=18,
    pady=8,
    relief="raised",
    borderwidth=2,
    highlightbackground="#d87cae",
    highlightthickness=1,
)

for btn in (button, rename_button, undo_button):
    btn.configure(
        highlightcolor="#d87cae",
        highlightbackground="#d87cae",
        overrelief="raised",
    )

status_label = tk.Label(root, textvariable=status_var, wraplength=560, bg=GREEN)
status_label.pack(pady=(0, 8))

preview_frame = tk.Frame(root, bg=GREEN)
preview_frame.pack(padx=12, pady=8, fill=tk.BOTH, expand=True)

before_label = tk.Label(preview_frame, text="Before", font=("Segoe UI", 10, "bold"), bg=GREEN)
before_label.grid(row=0, column=0, padx=6, pady=(0, 6), sticky="w")

after_label = tk.Label(preview_frame, text="After", font=("Segoe UI", 10, "bold"), bg=GREEN)
after_label.grid(row=0, column=1, padx=6, pady=(0, 6), sticky="w")

before_listbox = tk.Listbox(preview_frame, width=32, height=16, bg="#f4fff5")
before_listbox.grid(row=1, column=0, padx=(0, 8), sticky="nsew")

after_listbox = tk.Listbox(preview_frame, width=32, height=16, bg="#f4fff5")
after_listbox.grid(row=1, column=1, sticky="nsew")

preview_frame.grid_columnconfigure(0, weight=1)
preview_frame.grid_columnconfigure(1, weight=1)
preview_frame.grid_rowconfigure(1, weight=1)

root.mainloop()
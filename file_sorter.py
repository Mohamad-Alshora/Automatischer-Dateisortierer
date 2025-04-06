import os
import shutil
from config import WATCHED_FOLDER, EXTENSION_MAP

def get_category(filename):
    _, ext = os.path.splitext(filename.lower())
    for category, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return category
    return "Others"

def move_file(file_path):
    filename = os.path.basename(file_path)
    category = get_category(filename)
    target_folder = os.path.join(WATCHED_FOLDER, category)

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    target_path = os.path.join(target_folder, filename)

    # Falls Datei schon existiert, umbenennen
    if os.path.exists(target_path):
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(target_path):
            new_filename = f"{base}_{counter}{ext}"
            target_path = os.path.join(target_folder, new_filename)
            counter += 1

    shutil.move(file_path, target_path)
    print(f"[✓] '{filename}' → '{category}'")

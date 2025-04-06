import os

# Zielordner (z.B. Downloads)
WATCHED_FOLDER = os.path.expanduser("~/Downloads")

# Zielstruktur: Dateityp → Zielordnername
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Programs": [".exe", ".msi", ".apk"],
    "Scripts": [".py", ".js", ".sh"],
    "Others": []
}

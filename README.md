# 📂 Automatischer Dateisortierer

Dieses Tool überwacht einen Ordner (z. B. Downloads) und sortiert neue Dateien automatisch in Unterordner wie `Images`, `Documents`, `Videos` usw.

## ✅ Features
- Automatisches Erkennen von Dateitypen
- Verschiebt Dateien in passende Ordner
- Live-Überwachung mit `watchdog`
- Plattformübergreifend (Windows/Linux/Mac)

## 🔧 Installation

```bash
git clone https://github.com/dein-username/auto_sorter.git
cd auto_sorter
pip install -r requirements.txt
python main.py


🛠️ Configuration
1. Change the Folder Path
To change the monitored folder, open the config.py file and modify the WATCHED_FOLDER value. The path must be specified as an absolute path.

Example:

python
Copy
Edit
WATCHED_FOLDER = "/Users/yourusername/Downloads"
For Windows, the path could look like this:

python
Copy
Edit
WATCHED_FOLDER = r"C:\Users\yourusername\Downloads"
2. Adjust File Types and Target Folders
In the same config.py, you can also adjust the file categorization. By default, folders like Images, Documents, Videos, etc., are predefined. You can modify the file extensions in the lists of each category.

Example:

python
Copy
Edit
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Programs": [".exe", ".msi", ".apk"],
    "Others": []
}
📂 How It Works
The tool monitors the specified folder.

When a new file is added, the script detects its file type.

The file is automatically moved to the appropriate folder (e.g., Images, Documents).


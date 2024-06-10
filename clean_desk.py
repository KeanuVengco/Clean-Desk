import os
import shutil
import zipfile
from datetime import datetime

# Define path to desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Define a dictionary where keys are folder names and values are lists of file extensions
file_type_folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods", ".numbers"],
    "Presentations": [".ppt", ".pptx", ".key", ".odp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".bz2", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".ipynb", ".xml"],
    "Misc": [".json", ".yaml", ".yml", ".ini", ".cfg"],
    # Add more categories and extensions as needed
}

def create_folders():
    """Create folders on the desktop for each file type category."""
    for folder in file_type_folders.keys():
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files():
    """Move files into respective folders based on file extension."""
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        if os.path.isfile(item_path):
            _, file_extension = os.path.splitext(item)
            for folder, extensions in file_type_folders.items():
                if file_extension.lower() in extensions:
                    destination = os.path.join(desktop_path, folder, item)
                    shutil.move(item_path, destination)
                    break

def archive_desktop():
    """Archive the entire desktop into a zip file."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    zip_filename = os.path.join(desktop_path, f"Desktop_{date_str}.zip")
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as desktop_zip:
        for foldername, subfolders, filenames in os.walk(desktop_path):
            # Skip the newly created zip file
            filenames = [f for f in filenames if not f.startswith(f"Desktop_{date_str}.zip")]
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                # Add file to the zip file
                desktop_zip.write(file_path, os.path.relpath(file_path, desktop_path))

def clean_desktop():
    create_folders()
    move_files()
    print("Clean Desk: Your desktop has been cleaned and files are organized!")

def main():
    archive = input("Would you like to archive the entire desktop for today? (yes/no): ").strip().lower()
    if archive == 'yes':
        archive_desktop()
        print("Desktop archived successfully!")
    
    clean_desktop()

if __name__ == "__main__":
    main()

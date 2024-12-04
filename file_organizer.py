import shutil
from pathlib import Path

# Define file categories
FILE_CATEGORIES = {
    "pdf": "PDFs",
    "jpg": "Images",
    "png": "Images",
    "jpeg": "Images",
    "docx": "Docs",
    "txt": "Text",
    "mp4": "Videos",
    "mp3": "Audio"
}

def organize_files(directory):
    """
    Organizes files in the given directory into categorized sub-folders.
    
    Args:
        directory (str): The directory to organize.
    """
    # Convert directory to Path object
    directory_path = Path(directory).resolve()  # Convert to absolute path
    
    if not directory_path.exists():
        print(f"The directory {directory} does not exist.")
        return
    
    # Create categorized folders if they don't exist
    for file in directory_path.iterdir():
        if file.is_file():  # Skip directories
            file_extension = file.suffix.lower()[1:]  # Get the file extension without the dot
            folder_name = FILE_CATEGORIES.get(file_extension, "Miscellaneous")
            destination_folder = directory_path / folder_name
            destination_folder.mkdir(exist_ok=True)  # Ensure the folder exists
            
            # Move the file
            new_file_path = destination_folder / file.name
            if new_file_path.exists():
                # Handle duplicate by renaming
                base, ext = file.stem, file.suffix
                counter = 1
                while new_file_path.exists():
                    new_file_path = destination_folder / f"{base}_{counter}{ext}"
                    counter += 1
            
            shutil.move(str(file), str(new_file_path))
            print(f"Moved: {file} -> {new_file_path}")

if __name__ == "__main__":
    # Specify the directory to organize
    target_directory = input("Enter the directory to organize: ").strip()
    organize_files(target_directory)

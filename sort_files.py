import os
import shutil

# Define the categories and their corresponding file extensions
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".php"],
    "Executables": [".exe", ".bin", ".sh", ".bat"],
    # Add more categories and extensions as needed
}


def sort_files(folder_path):
    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        print(f"The folder path '{folder_path}' does not exist.")
        return

    # Create directories for each category if they don't already exist
    for category in CATEGORIES.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Iterate over files in the given folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file extension
        _, file_extension = os.path.splitext(filename)

        # Find the appropriate category for the file
        for category, extensions in CATEGORIES.items():
            if file_extension.lower() in extensions:
                # Move the file to the appropriate category folder
                dest_path = os.path.join(folder_path, category, filename)
                shutil.move(file_path, dest_path)
                print(f"Moved '{filename}' to '{category}'")
                break
        else:
            # If no category matches, move to 'Others' folder
            others_path = os.path.join(folder_path, "Others")
            if not os.path.exists(others_path):
                os.makedirs(others_path)
            dest_path = os.path.join(others_path, filename)
            shutil.move(file_path, dest_path)
            print(f"Moved '{filename}' to 'Others'")


# Example usage
folder_to_sort = r"C:\Users\SANYAM\Downloads"

sort_files(folder_to_sort)

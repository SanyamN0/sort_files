# sort_files
This script sorts files in a specified folder into subfolders based on their file extensions. The subfolders are created according to predefined categories, such as "Images", "Documents", "Videos", etc. If a file's extension does not match any predefined category, it is moved to an "Others" folder.


# A dictionary file_categories defines categories and their corresponding file extensions:
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".php"],
    "Executables": [".exe", ".bin", ".sh", ".bat"]
}

# Specify the path to the folder that you want to sort and call the sort_files function:

folder_to_sort = r"path\of\the\folder"
sort_files(folder_to_sort)

This will organize all files in the specified folder into subfolders based on their file types, making it easier to manage and locate files.

"""
Parameter: file path, by_date
Returns: destination folder path for the file (e.g. 'Images', 'Images/2026/October')

1. Give the extensions for files 

Case A: If by-date is unabled

Parameter: file path, by_date = False

A1. For each file, take its extension
A2. Check if the extension is in the list of extensions for each category
A3. If it is, return the category name as the destination folder path

Case B: If by-date is enabled

Parameter: file path, by_date = True

B1. For each file, take its extension
B2. Check if the extension is in the list of extensions for each category
B3. If it is, return the category name as the destination folder path
B4. Get the creation date of the file
B5. Create a folder path based on the creation date (e.g. 'Images/2026/October')
"""
from pathlib import Path
# for dates and hours
from datetime import datetime

# Extension categories for file classification
Categories = {
    "Documents": [".txt", ".pdf", ".docx", ".doc", ".csv", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bnp", ".bsp"],
    "Videos": [".mp3", ".mp4", ".wav", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".iso", ".7z"],
    "Binaries": [".bin", ".dat"],
    "C": [".c", ".h"],
    "C++": [".cpp", ".hpp"],
    "Python": [".py"],
    "Java": [".java"],
    "C#": [".cs"],
    "HTML": [".html"],
    "JavaScript": [".js"],
    "JSP": [".jsp"],
    "CSS": [".css"],
    "PHP": [".php"],
    "GO": [".go"],
    "Kotlin": [".kt"],
    "Executables": [".exe", ".class", ".dill", ".so"],
    "Matlab": [".m", ".mlx"],
    "Json": [".json"],
    "Debian Ubuntu": [".deb"],
    "Other": []
}

#def classify_file(path, by_date):
    
        
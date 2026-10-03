"""
Parameter: filename, optional date: if by-date is enabled
Returns: destination folder path for the file (e.g. 'Images', 'Images/2026/10')
"""

import os
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

#def classify_file(path):
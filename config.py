"""
Configuration file for File Organizer
Defines file type categories
"""

# File type categories - add or modify as needed
FILE_CATEGORIES = {
    'Images': [
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp',
        '.ico', '.tiff', '.psd', '.raw', '.heic'
    ],
    'Documents': [
        '.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.pptx',
        '.ppt', '.odt', '.rtf', '.tex', '.csv', '.md'
    ],
    'Videos': [
        '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm',
        '.m4v', '.mpg', '.mpeg', '.3gp'
    ],
    'Audio': [
        '.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a',
        '.opus', '.ape'
    ],
    'Archives': [
        '.zip', '.rar', '.tar', '.gz', '.7z', '.bz2', '.xz',
        '.tar.gz', '.tgz', '.deb', '.rpm'
    ],
    'Code': [
        '.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h',
        '.json', '.xml', '.php', '.rb', '.go', '.rs', '.swift',
        '.kt', '.ts', '.jsx', '.tsx', '.vue', '.sh', '.bat'
    ],
    'Executables': [
        '.exe', '.msi', '.app', '.deb', '.dmg', '.pkg', '.apk'
    ],
    'Books': [
        '.epub', '.mobi', '.azw', '.azw3'
    ],
}

def get_category(extension):
    """
    Get the category for a file extension.
    
    Args:
        extension: File extension (e.g., '.pdf')
        
    Returns:
        Category name or 'Other' if not found
    """
    extension = extension.lower()
    
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    
    return 'Other'

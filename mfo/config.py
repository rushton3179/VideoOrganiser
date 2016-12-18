import os
from VideoOrganiser.settings import BASE_DIR

# Base dir where out media will be stored
BASE_DIR_FILES = '/Users/ryanrushton/Movies'

# The dir that the VideoOrganiser watches for new files
WATCHED_DIR = '/Users/ryanrushton/New Media'

# The dir that VideoOrganiser uploads new files to (moved to watched dir after completion
UPLOAD_DIR = os.path.join(BASE_DIR, 'Uploads')

# Whether VideoOrganiser is currently watching above dir
IS_WATCHING = False

# Aloud file types
ALLOWED_EXTENSIONS = [
    'mp4',
    'avi',
    'm4p',
    'mp4v',
    'mkv'
]
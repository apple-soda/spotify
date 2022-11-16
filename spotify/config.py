"""Spotift development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = ("b'4\xe20\xed\x81\x9es\xa2\xa7\xbaV\xd1",
              "\xfb\x85ks\xb3\xe8,P\xed\xa0\xb0}'")
SESSION_COOKIE_NAME = 'login'

# File upload to var/uploads/ (if needed)
SPOTIFY_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = SPOTIFY_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/spotify/sqlite3 (if needed)
DATABASE_FILENAME = SPOTIFY_ROOT/'var'/'spotify.sqlite3'
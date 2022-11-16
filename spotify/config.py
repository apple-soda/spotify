"""Spotift development configuration."""

import pathlib
import requests

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

# # SECRET SHIT (CHANGE FOR GITHUB PUSHES)
# # id and shit
# CLIENT_ID = '9bc3dea17d8e4cb98694606b0bd7c618'
# CLIENT_SECRET = 'a8c34b47f88940e498031d554aa96430'
# AUTH_URL = 'https://accounts.spotify.com/api/token'
# BASE_URL = 'https://api.spotify.com/v1/'

# # POST
# auth_response = requests.post(AUTH_URL, {
#     'grant_type': 'client_credentials',
#     'client_id': CLIENT_ID,
#     'client_secret': CLIENT_SECRET,
# })

# auth_response_data = auth_response.json()
# access_token = auth_response_data['access_token']

# headers = {
#     'Authorization': 'Bearer {token}'.format(token=access_token)
# }

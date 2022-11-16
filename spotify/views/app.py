"""Spotify main view."""
from flask import render_template, request
import requests
import spotify
import spotify.views.utils as utils

# SECRET SHIT (CHANGE FOR GITHUB PUSHES)
# id and shit
CLIENT_ID = '9bc3dea17d8e4cb98694606b0bd7c618'
CLIENT_SECRET = 'a8c34b47f88940e498031d554aa96430'
AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'


# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']


headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}


@spotify.app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        link = request.form['link']

        # do some transformations
        track_id = link.split('/')[-1].split('?')[0]
        playlist_id = link.split('/')[-1]

        raw_playlist_data = utils.get_raw_playlist_data(
            BASE_URL, playlist_id, headers)
        playlist_list = utils.get_entire_playlist(BASE_URL, track_id, headers)
        artists_d = utils.get_artist_count(playlist_list)

        playlist_img_url = raw_playlist_data['images'][0]['url']
        num_artist = 5
        top_artists = list(artists_d.keys())[-num_artist:][::-1]

        context = {
            "playlist_img_url": playlist_img_url,
            "raw_playlist_data": raw_playlist_data,
            "artists_d": artists_d,
            "top_artists": top_artists
        }
        
        return render_template('analytics.html', **context)
    return render_template('index.html')

"""Spotify main view."""
import flask
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


@spotify.app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'POST':
        flask.session['link'] = flask.request.form['link']
        return flask.redirect(flask.url_for('show_analytics'))
    return flask.render_template('index.html')


@spotify.app.route('/analytics')
def show_analytics():
    link = flask.session['link']

    # do some transformations
    track_id = link.split('/')[-1].split('?')[0]
    playlist_id = link.split('/')[-1]

    raw_playlist_data = utils.get_raw_playlist_data(
        BASE_URL, playlist_id, headers)

    # if raw_playlist_data[]
    if not isinstance(raw_playlist_data, dict):
        print("is not a dict")
        return raw_playlist_data  # actually return redirect to index.html

    playlist_list = utils.get_entire_playlist(BASE_URL, track_id, headers)
    artists_d = utils.get_artist_count(playlist_list)
    album_d = utils.get_album_count(playlist_list)

    playlist_name = raw_playlist_data['name']

    playlist_img_url = raw_playlist_data['images'][0]['url']

    num_artist = 10
    num_album = 5

    # god genius coder matty right here fr
    a = list(artists_d.keys())[-num_artist:][::-1]
    c = list(artists_d.values())[-num_artist:][::-1]
    top_artists = [[i, j] for i, j in zip(a, c)]
    top_artist_count = max(c)  # helpful for scaling the visualizations

    a = list(album_d.keys())[-num_album:][::-1]
    c = [i[0] for i in list(album_d.values())[-num_artist:][::-1]]
    c_urls = [i[1]['url']
              for i in list(album_d.values())[-num_artist:][::-1]]

    top_albums = [[i, j, k] for i, j, k in zip(a, c, c_urls)]

    context = {
        "playlist_name": playlist_name,
        "playlist_img_url": playlist_img_url,
        "raw_playlist_data": raw_playlist_data,
        "artists_d": artists_d,
        "top_artists": top_artists,
        "top_artist_count": 30,
        "top_albums": top_albums
    }
    return flask.render_template('analytics.html', **context)


@spotify.app.route('/', methods=['GET'])
def back_home():
    return flask.redirect(flask.url_for('main'))

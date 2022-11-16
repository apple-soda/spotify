import requests


def get_raw_playlist_data(base_url, playlist_id, headers):
    r = requests.get(
        base_url + 'playlists/' + playlist_id + '/tracks',
        headers=headers,
        params={'offset': 0}
    )
    d = r.json()
    return d


def get_entire_playlist(base_url, track_id, headers):
    master_list = []
    offset = 0

    r = requests.get(
        base_url + 'playlists/' + track_id + '/tracks',
        headers=headers,
        params={'offset': offset}
    )

    d = r.json()
    master_list += d['items']

    while len(d['items']) > 0:
        offset += 100
        r = requests.get(
            base_url + 'playlists/' + track_id + '/tracks',
            headers=headers,
            params={'offset': offset}
        )
        d = r.json()
        master_list += d['items']

    return master_list


def get_artist_count(master_list):
    # ['track']['artists']: list of artists
    # ['track']['artists'][0]['name'] : name of first artist
    artists = {}

    for i in master_list:
        an = i['track']['artists'][0]['name']
        if an in artists:
            artists[an] += 1
        else:
            artists[an] = 1

    return dict(sorted(artists.items(), key=lambda item: item[1]))


def get_album_count(master_list):
    # ['track']['album']['name'] : album name
    # ['track']['album']['images'][0] : album image
    return None

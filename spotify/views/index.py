"""Spotify main view."""
import spotify

@spotify.app.route('/')
def index():
    """Display '/' route."""
    # do shit
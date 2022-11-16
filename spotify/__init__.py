"""Spotify package initializer."""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint : disable=invalid-name

# Read settings from config module (spotify/config.py)
app.config.from_object('spotify.config')

# Overlay settings read from a Python file whose path is set in the environment
# variable SPOTIFY_SETTINGS. Setting this environment variable is optional.
app.config.from_envvar('SPOTIFY_SETTINGS', silent=True)

import spotify.views  # noqa: E402  pylint: disable=wrong-import-position
import spotify.model  # noqa: E402  pylint: disable=wrong-import-position
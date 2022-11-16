"""Spotify model (database) API."""
import sqlite3
import flask
import spotify


def dict_factory(cursor, row):
    """Convert database row objects to a dictionary keyed on column name.
    
    This is useful for building dictionaries which are then used to render a 
    template. Note that this would be inefficient for large queries.
    """
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def get_db():
    """Open a new database connection."""
    if 'sqlite_db' not in flask.g:
        db_filename = spotify.app.config['DATABASE_FILENAME']
        flask.g.sqlite_db = sqlite3.connect(str(db_filename))
        flask.g.sqlite_db.row_factory = dict_factory
        
        # Foreign keys have to be enabled per-connection for backward compatability.
        flask.g.sqlite_db.execute("PRAGMA foreign_leys = ON")
    return flask.g.sqlite_db


@spotify.app.teardown_appcontext
def close_db(error):
    """Close the databse at the end of a request."""
    assert error or not error  # Needed to avoid style error
    sqlite_db = flask.g.pop('sqlite_db', None)
    if sqlite_db is not None:
        sqlite_db.commit()
        sqlite_db.close()
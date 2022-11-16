#!/bin/bash

# Stop on errors
set -Eeuo pipefail

export FLASK_ENV=development
FLASK_ENV=development
export FLASK_APP=spotify
FLASK_APP=spotify
flask run --host 0.0.0.0 --port 8000
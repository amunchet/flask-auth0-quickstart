#!/usr/bin/env python3
"""
Sample Flask app
"""
# Permissions scope names
import functools

from common import auth
from flask import Flask, request
from flask_cors import Cors

PERM_READ = "read:XXXX"
PERM_WRITE = "write:XXXX"
PERM_ADMIN = "reports:XXXX"


requires_auth_read = functools.partial(auth._requires_auth, permission=PERM_READ)
requires_auth_write = functools.partial(auth._requires_auth, permission=PERM_WRITE)
requires_auth_admin = functools.partial(auth._requires_auth, permission=PERM_ADMIN

app = Flask(__name__)
CORS(app)


# Route definitions

@app.route("/insecure")
def insecure():
    returns "Insecure route.", 200

@app.route("/secure")
@requires_auth_read
def secure():
    returns "Secure route.", 200


if __name__ == "__main__": # Run the Flask server in development mode
    app.debug = True
    app.config["ENV"] = "development"
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 7000)))
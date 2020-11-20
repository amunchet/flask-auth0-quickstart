# Flask-Auth0 Quickstart Scaffolding Template
This is a simple project to quickstart a project using Flask (Python), Docker, and Auth0 authentication.

## Requirements
- Docker.  Docker-compose is recommended, but not required.
- Python3 (for the setup script)


## Setup Instructions
0.  Clone this repository `git clone https://github.com/amunchet/flask-auth0-quickstart.git`
1.  `cd flask-auth0-quickstart`
2.  `./setup.py` (or `python setup.py`)
3.  Follow the instructions.
4.  Enjoy!


## Tests
There are some basic tests to make sure the URLs are protected.  


## Typical Next Steps
Moving the snippet out, etc. 

## Trying out the authentication
To try out the authentication, you will need your Authorization Header from an already authenticated request.  Copy that (it should begin wtih "Bearer ...")

1.  `import requests`
2.  `a = requests.get("http://localhost:[PORT]/secure", headers={"Authorization" : "Bearer ..."})`

3.  If you did not set your user to have permissions `read`, the request will return `401`.  Otherwise, `a.text` contain "Secure route."

If you have a problem, check to make sure your Auth0 permissions are configured correctly for your user.

## Design Notes

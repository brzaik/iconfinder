# iconfinder
An interactive icon finder UI to be used with icon libraries.

## Python Setup

Clone or download the files to a common place, such as `/var/www/html/iconfinder` if using Apache.

From within the `iconfinder` top-level directory:

`pip install -r requirements.txt`
`virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r requirements.txt`

Set up a mysql database and fill in the config details in `config.py` to connect to the database.

Initialize the database: `python db_create.py`

Run the app: python `run.py runserver`
Create a new migration: `python run.py db revision`

### Setup Gotchas

You may run into issues with errors like `Failed building wheel for PyICU`. Try running this on Ubuntu/Debian:

`sudo apt-get install build-essential libssl-dev libffi-dev python-dev libicu-dev`

(More info at https://stackoverflow.com/questions/22073516/failed-to-install-python-cryptography-package-with-pip-and-setup-py)

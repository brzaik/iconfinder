##########################################################
#
# Config File for IconFinder App
#
##########################################################
import os


# grab the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

# Update later by using a random number generator and moving
# the actual key outside of the source code under version control
SECRET_KEY = os.urandom(24).encode('hex')
WTF_CSRF_ENABLED = True
DEBUG = True

# SQLAlchemy
## FILL IN VALUES
MYSQL_USER = ''
MYSQL_PASSWORD = ''
MYSQL_DB = ''
MYSQL_HOST = ''
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + MYSQL_USER + ':' + MYSQL_PASSWORD + MYSQL_HOST + MYSQL_DB + '?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Bcrypt algorithm hashing rounds
BCRYPT_LOG_ROUNDS = 15

# Uploads
DROPZONE_UPLOAD_MULTIPLE = True  # enable parallel upload
DROPZONE_PARALLEL_UPLOADS = 3  # handle 3 file per request
DROPZONE_ALLOWED_FILE_CUSTOM = True
DROPZONE_ALLOWED_FILE_TYPE = '.svg,.png,.jpg,.jpeg,.gif'
DROPZONE_MAX_FILES = 30

UPLOADS_DEFAULT_DEST = TOP_LEVEL_DIR + '/iconfinder/static/uploads/'
UPLOADED_IMAGES_DEST = TOP_LEVEL_DIR + '/iconfinder/static/uploads/'

# Source Repositories
STATIC_DIR = TOP_LEVEL_DIR + '/iconfinder/static/'
SOURCES_DEFAULT_DEST = TOP_LEVEL_DIR + '/iconfinder/static/repo'

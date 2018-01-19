***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED*** imports ***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***

***REMOVED***
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, json
from flask_assets import Environment, Bundle
from flask_uploads import UploadSet, IMAGES, configure_uploads
from iconfinder.database import db_session

***REMOVED*** Database Model
from iconfinder.models import Icon, Category, Source


***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED*** config ***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***


***REMOVED*** Initialize app
app = Flask(__name__, instance_relative_config=True)
assets = Environment(app)

***REMOVED*** Uploads

***REMOVED*** grab the folder of the top-level directory of this project
***REMOVED*** ***REMOVED***
***REMOVED*** ***REMOVED***
***REMOVED***
***REMOVED*** ***REMOVED***
***REMOVED*** UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/uploads/'
***REMOVED***
***REMOVED*** ***REMOVED***
***REMOVED*** UPLOADED_IMAGES_URL = 'http://localhost:5000/static/uploads/'


***REMOVED*** load flask-assets bundles
scss = Bundle('*.scss', filters='scss', output='css/sass.css')
all_css = Bundle(scss, filters='cssmin', output="css/all.css")
assets.register('all_css', all_css)

***REMOVED*** set livereload for app
app.debug = True
app.jinja_env.auto_reload = True

***REMOVED*** Configure the image uploading via Flask-Uploads
***REMOVED*** images = UploadSet('images', IMAGES)
***REMOVED*** configure_uploads(app, images)


app.config.from_object(__name__)
app.config.update(dict(
    JSONIFY_PRETTYPRINT_REGULAR=False
))
app.config.from_envvar('FLASK_SERVER_SETTINGS', silent=True)


@app.teardown_appcontext
def shutdown_dbsession(exception=None):
    db_session.remove()


***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED*** blueprints ***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***

***REMOVED******REMOVED******REMOVED******REMOVED*** NOTHING DEFINED ***REMOVED******REMOVED******REMOVED******REMOVED***


***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED*** routes ***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

***REMOVED*** Default Route: Show icon library
@app.route("/")
def index():
    icons = db_session.query(Icon).all()
    return render_template('index.html', title='IconFinder',icons=icons)


***REMOVED*** Icon Uploading
@app.route('/upload/')
def upload():
    return render_template('upload.html', title='Upload to Icon Library')

***REMOVED*** Icon Uploading
@app.route('/sources/')
def sources_list():
    return render_template('sources.html', title='Manage Icon Sources')


@app.route('/process_upload', methods=["POST"])
def process_upload():
    uploaded_files = request.files.getlist("file[]")
    return ""


***REMOVED******REMOVED*** TEST ROUTES
***REMOVED*** test hello
@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('index.html',name=name)

***REMOVED*** sample api route
@app.route('/api/icons/')
def icons():
    icons = db_session.query(Icon).all()
    return json.jsonify([icon.to_dict() for icon in icons])

@app.route('/api/categories/')
def categories():
    categories = db_session.query(Category).all()
    return json.jsonify([category.to_dict() for category in categories])


if __name__ == "__main__":
    app.run()

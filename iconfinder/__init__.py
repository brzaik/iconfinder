from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, json
from flask_assets import Environment, Bundle
from iconfinder.database import db_session
from iconfinder.models import Icon

app = Flask(__name__)
assets = Environment(app)

scss = Bundle('*.scss', filters='scss', output='gen/sass.css')
all_css = Bundle(scss, filters='cssmin', output="css/all.css")
assets.register('all_css', all_css)


***REMOVED*** set livereload for app
app.debug = True


app.config.from_object(__name__)
app.config.update(dict(
    JSONIFY_PRETTYPRINT_REGULAR=False
))
app.config.from_envvar('FLASK_SERVER_SETTINGS', silent=True)

@app.teardown_appcontext
def shutdown_dbsession(exception=None):
    db_session.remove()


***REMOVED*** Default Route: Show icon library
@app.route("/")
def index():
    return render_template('index.html', title='IconFinder')


***REMOVED*** Icon Listing View
@app.route('/upload/')
def upload():
    return render_template('upload.html', title='Upload to Icon Library')


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



if __name__ == "__main__":
    app.run()

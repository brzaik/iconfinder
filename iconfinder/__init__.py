***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED*** imports ***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***

from os.path import join, isfile

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, json
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

from config import *


***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED*** config ***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***


***REMOVED*** Initialize app
app = Flask(__name__, instance_relative_config=True)

assets = Environment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


***REMOVED*** load flask-assets bundles
scss = Bundle('*.scss', filters='scss', output='css/sass.css')
all_css = Bundle(scss, filters='cssmin', output="gen/all.css")
assets.register('all_css', all_css)

all_js = Bundle('js/*.js', filters='rjsmin', output="gen/all.min.js")
assets.register('all_js', all_js)

***REMOVED*** set livereload for app
app.debug = True
app.jinja_env.auto_reload = True


app.config.from_object(__name__)
app.config.update(dict(
    JSONIFY_PRETTYPRINT_REGULAR=False
))
app.config.from_envvar('FLASK_SERVER_SETTINGS', silent=True)


***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED*** blueprints ***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***

from iconfinder.sources.views import sources_blueprint
from iconfinder.icons.views import icons_blueprint

***REMOVED*** register the blueprints
app.register_blueprint(sources_blueprint)
app.register_blueprint(icons_blueprint)


***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED*** routes ***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***

class CategoryForm(Form):
    name = TextField('Name:', validators=[validators.required()])

    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)


***REMOVED*** Database Model
from iconfinder.models import Icon, Category, Source


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

***REMOVED*** Default Route: Show icon library
@app.route("/", methods=['GET', 'POST'])
def index():
    form = CategoryForm(request.form)

    icons = Icon.query.order_by(Icon.shortname).all()
    categories = Category.query.order_by(Category.name).all()

    print form.errors
    if request.method == 'POST':
        name = request.form['name']

        if form.validate():
            flash('New category was successfully added.')
            category = Category(name)
            db.session.add(category)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            flash('Please fill in the required fields and try again.')

    return render_template('index.html', title='IconFinder',icons=icons, categories=categories, form=form)

@app.route('/categories/<category_id>/delete')
def delete_category(category_id):
    category = Category.query.filter_by(id=category_id).first_or_404()

    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('index'))


***REMOVED*** Icon Uploading
@app.route('/upload/')
def upload():
    return render_template('upload.html', title='Upload to Icon Library')

@app.route('/process_upload', methods=["POST"])
def process_upload():
    uploaded_files = request.files.getlist("file[]")
    return ""


***REMOVED*** sample api route
@app.route('/api/icons/')
def icons():
    icons = Icon.query.all()
    return json.jsonify([icon.to_dict() for icon in icons])

@app.route('/api/categories/')
def categories():
    categories = Category.query.all()
    return json.jsonify([category.to_dict() for category in categories])


if __name__ == "__main__":
    manager.run()

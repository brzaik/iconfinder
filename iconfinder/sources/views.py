***REMOVED*** iconfinder/sources/views.py

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED*** imports ***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***

***REMOVED***
from os.path import join

from flask import render_template, Blueprint, request, redirect, url_for, flash, abort
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from iconfinder import app, db
from git import *

***REMOVED*** Database Model
from iconfinder.models import Source, Icon, Category

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED*** config ***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***

sources_blueprint = Blueprint('sources', __name__)


class SourceForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    repo_type = TextField('Repo Type:', validators=[validators.required()])
    url = TextField('URL:', validators=[validators.required()])

    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)


***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED*** helper functions ***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***

***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED*** routes ***REMOVED******REMOVED******REMOVED******REMOVED***
***REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED******REMOVED***

@sources_blueprint.route('/sources/', methods=['GET', 'POST'])
def sources_list():
    sources = Source.query.all()
    form = SourceForm(request.form)

    print form.errors
    if request.method == 'POST':
        name = request.form['name']
        repo_type = request.form['repo_type']
        url = request.form['url']

        if form.validate():
            flash('New source was successfully added.')
            source = Source(name, repo_type, url)
            db.session.add(source)
            db.session.commit()
            return redirect(url_for('sources.sources_list'))
        else:
            flash('Please fill in the required fields and try again.')

    return render_template('sources.html', title='Manage Icon Sources', form = form, sources = sources)


@sources_blueprint.route('/sources/<source_id>/delete')
def delete_source(source_id):
    source = Source.query.filter_by(id=source_id).first_or_404()

    db.session.delete(source)
    db.session.commit()
    return redirect(url_for('sources.sources_list'))


***REMOVED******REMOVED*** TO-DO:
***REMOVED***   - Need to provide for cases in which there are updates to the source repo but it has already been cloned
***REMOVED***   - Need to ensure duplicates within the same source repo are not added to db

@sources_blueprint.route('/sources/refresh')
def sources_refresh():
    supported_filetypes = ['.svg', '.png', '.jpg', '.jpeg', '.gif']
    t_supported_filetypes = tuple(supported_filetypes)

    sources = Source.query.all()

    for source in sources:
        repo_path = join(app.config['SOURCES_DEFAULT_DEST'], str(source.id))
        if os.path.exists(repo_path):
            pass
        else:
            new_repo = Repo.clone_from(source.url, repo_path)

        for root, dirs, files in os.walk(repo_path):
            for file in files:
                if file.lower().endswith(t_supported_filetypes):
                    icon_shortname = file.split('.')[0]
                    icon_mimetype = file.split('.')[1]
                    icon_localpath = root.split(app.config['STATIC_DIR'])[1] + "/" + file
                    icon = Icon(shortname=icon_shortname, mimetype=icon_mimetype, localpath=icon_localpath, source_id=source.id)
                    db.session.add(icon)
                    db.session.commit()

    return render_template('sources_refresh.html', title='Refresh Icons')

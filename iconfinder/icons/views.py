# iconfinder/sources/views.py

#################
#### imports ####
#################

import os
from os.path import join

from flask import render_template, Blueprint, request, redirect, url_for, flash, abort, jsonify
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from iconfinder import app, db
from git import *

# Database Model
from iconfinder.models import Source, Icon, Category

################
#### config ####
################

icons_blueprint = Blueprint('icons', __name__)


##########################
#### helper functions ####
##########################

################
#### routes ####
################

@icons_blueprint.route('/icon/<icon_id>')
def icon_show(icon_id):
    icon = Icon.query.filter_by(id=icon_id).first_or_404()
    source = Source.query.filter_by(id=icon.source_id).first()
    category = Category.query.filter_by(id=icon.category_id).first()

    return render_template('icon.html', icon=icon, source=source, category=category)

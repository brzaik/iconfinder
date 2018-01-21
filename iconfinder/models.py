from iconfinder import db, app

class Icon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortname = db.Column(db.String(500))
    mimetype = db.Column(db.String(20))
    image_filename = db.Column(db.String(500), default=None, nullable=True)
    image_url = db.Column(db.String(500), default=None, nullable=True)
    localpath = db.Column(db.String(500), default=None, nullable=True)
    source_id = db.Column(db.Integer, unique=True)
    category_id = db.Column(db.Integer, unique=True)

    def __init__(self, shortname=None, mimetype=None, image_filename=None, image_url=None, localpath=None, source_id=None, category_id=None):
        self.shortname = shortname
        self.mimetype = mimetype
        self.image_filename = image_filename
        self.image_url = image_url
        self.localpath = localpath
        self.source_id = source_id
        self.category_id = category_id

    def __repr__(self):
        return "<Icon(id=%d, shortname='%s', mimetype='%s', localpath='%s', source_id='%s')>" % (self.id, self.shortname, self.mimetype, self.localpath, self.source_id, self.category_id)

    def to_dict(self):
        return {
            'id': self.id,
            'shortname': self.shortname,
            'mimetype': self.mimetype,
            'localpath': self.localpath,
            'source_id': self.source_id,
            'category_id': self.category_id
        }

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "<Category(id=%d, name='%s')>" % (self.id, self.name)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    repo_type = db.Column(db.String(20), unique=True)
    url = db.Column(db.String(500), unique=True)

    def __init__(self, name=None, repo_type=None, url=None):
        self.name = name
        self.repo_type = repo_type
        self.url = url

    def __repr__(self):
        return "<Source(id=%d, name='%s', repo_type='%s', url='%s')>" % (self.id, self.name, self.repo_type, self.url)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'repo_type': self.repo_type,
            'url': self.url
        }

from sqlalchemy import Column, Integer, String
from iconfinder.database import Base

class Icon(Base):
    __tablename__ = 'icons'

    id = Column(Integer, primary_key=True)
    shortname = Column(String(20), unique=True)
    mimetype = Column(String(20))
    image_filename = Column(String(500), default=None, nullable=True)
    image_url = Column(String(500), default=None, nullable=True)

    def __init__(self, shortname=None, mimetype=None, image_filename=None, image_url=None):
        self.shortname = shortname
        self.mimetype = mimetype
        self.image_filename = image_filename
        self.image_url = image_url

    def __repr__(self):
        return "<Icon(id=%d, shortname='%s', mimetype='%s')>" % (self.id, self.shortname, self.mimetype)

    def to_dict(self):
        return {
            'id': self.id,
            'shortname': self.shortname,
            'mimetype': self.mimetype
        }

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "<Category(id=%d, name='%s')>" % (self.id, self.name)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Source(Base):
    __tablename__ = 'sources'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    repo_type = Column(String(20), unique=True)
    url = Column(String(500), unique=True)

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

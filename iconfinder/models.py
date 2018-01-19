from sqlalchemy import Column, Integer, String
from iconfinder.database import Base

class Icon(Base):
    __tablename__ = 'icons'

    id = Column(Integer, primary_key=True)
    shortname = Column(String(20), unique=True)
    mimetype = Column(String(20))

    def __init__(self, shortname=None, mimetype=None):
        self.shortname = shortname
        self.mimetype = mimetype

    def __repr__(self):
        return "<Icon(id=%d, shortname='%s', mimetype='%s')>" % (self.id, self.shortname, self.mimetype)

    def to_dict(self):
        return {
            'id': self.id,
            'shortname': self.shortname,
            'mimetype': self.mimetype
        }

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'mysql+pymysql://craftcms:T5M22cux1Pu7tFUZ@localhost/iconfinder?charset=utf8',
    connect_args = {
        'port': 3306
    },
    echo='debug',
    echo_pool=True
)

db_session = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False
    )
)

Base = declarative_base()

def init_db():
    import iconfinder.models
    Base.metadata.create_all(engine)

    from iconfinder.models import Icon
    db_session.add_all([
        Icon(shortname='edit', mimetype='svg'),
        Icon(shortname='add', mimetype='svg')
    ])
    db_session.commit()

    print 'Initialized the database.'

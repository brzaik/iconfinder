# Check the PYTHONPATH environment variable before beginning to ensure that the
# top-level directory is included.  If not, append the top-level.  This allows
# the modules within the .../project/ directory to be discovered.
import sys
import os


print('Creating database tables for IconFinder app...')

if os.path.abspath(os.curdir) not in sys.path:
    print('...missing directory in PYTHONPATH... added!')
    sys.path.append(os.path.abspath(os.curdir))


# Create the database tables, add some initial data, and commit to the database
from iconfinder import db
from iconfinder.models import Icon, Category, Source

# Drop all of the existing database tables
db.drop_all()

# Create the database and the database table
db.create_all()

# Insert icon data
icon1 = Icon(shortname='edit', mimetype='svg')
icon2 = Icon(shortname='add', mimetype='svg')
db.session.add(icon1)
db.session.add(icon2)

# Commit the changes for the users
db.session.commit()

# Insert category data
category1 = Category(name='Uncategorized')
db.session.add(category1)

# Commit the changes for the recipes
db.session.commit()

print('...done!')

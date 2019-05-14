# services/users/manage.py

import unittest


from flask.cli import FlaskGroup

from project import db  # new    
from project import create_app
from project.api.models import User # new

app = create_app() # new
cli = FlaskGroup(create_app=create_app) # new

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    """Ejecutar los tests sin covertura de codigo"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command('seed_db')
def seed_db():
    """Sembrando en la base de datos."""
    db.session.add(User(username='cardenas', email='yersoncardenas@upeu.edu.pe'))
    db.session.add(User(username='jerson', email='cardenas.x7@gmail.com'))
    db.session.commit()


    
if __name__ == '__main__':
    cli()

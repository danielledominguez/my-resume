from flask_script import Manager
from resume import app, db, Professor

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    harrywang = Professor(name='Harry Wang', department='MIS')
    db.session.add(harrywang)
    db.session.commit()


if __name__ == "__main__":
    manager.run()

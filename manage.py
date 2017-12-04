from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    harrywang = Professor(name='Harry Wang', department='MIS')
    andreaeverard = Professor(name='Andrea Everard', department='MIS')
    course1 = Course(title='Management of Information Systems', number='MISY427', description="Explores practical applications of information technology in all aspects of management including organizational behavior, human resource management, international management and strategic decision making. Issues of managing emerging technologies, integrating technologies with people, organizational culture and structure and strategic decision making will be discussed.", professor=andreaeverard)
    course2 = Course(title='Business Application Development II', number='MISY350', description="Covers concepts related to client side development, including cascading style sheets and JavaScript.",professor=harrywang)
    course3 = Course(title='MIS Project Management', number='MISY431',description="Students learn project management techniques, and working in teams, apply this knowledge by developing technology-based business solutions for various enterprises.",professor=andreaeverard)
    db.session.add(harrywang)
    db.session.add(andreaeverard)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.commit()


if __name__ == "__main__":
    manager.run()

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    #return '<h1>hello world!!!! lalala</h1>'
    return render_template('index.html')


@app.route('/courses')
def get_all_courses():
    courses = [
        'MISY350: Business Application Development II',
        'MISY430: Systems Analysis and Implementation',
        'MISY427: Management of Information Systems'
    ]
    return render_template('courses.html', courses=courses)


@app.route('/about')
def get_about():
    #return '<h1>hello %s your age is %d </h1>' % (name,3)
    return render_template('about.html')


if __name__ == '__main__':
    app.run()

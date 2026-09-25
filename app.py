from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT
        )
    ''')

    conn.commit()
    conn.close()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students (name, email, password) VALUES (?, ?, ?)",
            (name, email, password)
        )

        conn.commit()
        conn.close()

        return render_template('register_success.html')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE email=? AND password=?",
            (email, password)
        )

        student = cursor.fetchone()

        conn.close()

        if student:
            return render_template('dashboard.html')
        else:
            return "Invalid Email or Password"

    return render_template('login.html')
@app.route('/interview')
def interview():
    return render_template('interview.html')


@app.route('/companies')
def companies():
    return render_template('companies.html')
@app.route('/infosys')
def infosys():
    return render_template('infosys.html')
@app.route('/tcs')
def tcs():
    return render_template('tcs.html')


@app.route('/wipro')
def wipro():
    return render_template('wipro.html')


@app.route('/accenture')
def accenture():
    return render_template('accenture.html')


@app.route('/capgemini')
def capgemini():
    return render_template('capgemini.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@app.route('/logout')
def logout():
    return render_template('index.html')


@app.route('/students')
def students():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    conn.close()

    return str(data)


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():

    if request.method == 'POST':

        score = 0

        if request.form.get('q1') == 'Programming Language':
            score += 1

        if request.form.get('q2') == 'HyperText Markup Language':
            score += 1

        if request.form.get('q3') == 'Styling':
            score += 1

        if request.form.get('q4') == 'Database':
            score += 1

        if request.form.get('q5') == 'Python Framework':
            score += 1

        return render_template('result.html', score=score)

    return render_template('quiz.html')


if __name__ == '__main__':
    create_table()
    app.run(debug=True)
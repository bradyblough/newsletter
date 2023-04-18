from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('newsletter.db', check_same_thread=False)
cursor = connection.cursor()



@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor.execute(f'insert into newsletter(name, email) values(?, ?)', (name, email))
        connection.commit()
        msg = 'Your info has been received.'
        print(cursor.fetchall())
        return render_template('index.html', msg=msg)
    else:
        return render_template('index.html')


app.run(debug=True)

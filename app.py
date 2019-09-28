from flask import Flask, render_template, request, session
import csv
import os

app = Flask(__name__)
app.secret_key = os.urandom(123)

file = open('chats.csv', 'a')
file.close()
# status['login'] = None
# status['update'] = None

@app.route('/')
def home():
    # session['name'] = session['animal'] = None
    # name = animal = None
    return render_template('home.html')

@app.route('/finroom', methods=['get','post'])
def room():
    # chat = request.form.get('chat')
    # name = request.form.get('name')
    # animal = request.form.get('animal')

    if request.form.get('name') and request.form.get('animal'): #login
        session['name'] = request.form.get('name')
        session['animal'] = request.form.get('animal')
        # session['name'] = name
        # session['animal'] = animal
        file = open('chats.csv', 'r')
        reader = csv.reader(file)
        chats = list(reader)
        file.close()
        chats.reverse()
        return render_template('finroom.html', chats=chats)
    elif request.form.get('chat') and session['name'] and session['animal']:
        # chat = request.form.get('chat')
        # name = session['name']
        # animal = session['animal']
        file = open('chats.csv', 'a')
        writer = csv.writer(file)
        writer.writerow((session['name'], session['animal'], request.form.get('chat')))
        file.close()
        file = open('chats.csv', 'r')
        reader = csv.reader(file)
        chats = list(reader)
        file.close()
        chats.reverse()
        return render_template('finroom.html', chats=chats)
    else:
        try:
            session['name'] and session['animal']
            file = open('chats.csv', 'r')
            reader = csv.reader(file)
            chats = list(reader)
            file.close()
            chats.reverse()
            return render_template('finroom.html', chats=chats)
        except:
            return 'Error. Masukkan name dan pilih animal!'

@app.route('/logout')
def logout():
    # session.pop('name')
    # session.pop('animal')
    session.clear()
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, send_from_directory, redirect, request, jsonify, session, send_file
import sqlite3
import random
import os

# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT,
#         password TEXT
#     )
# ''')

app = Flask(__name__)
app.secret_key = 'abcabcabc'

app.config.update(
    SESSION_COOKIE_HTTPONLY = False
)

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'gateway.html')
    # return 'Hello, World!'

@app.route('/', methods=['POST'])
def index_post():
    return redirect('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81')

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81')
def mainPage():
    return render_template('index.html')

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a82')
def haha():
    filename = request.args.get('filename')
    filepath = f"./static/{filename}"  # This is insecure!
    print(filepath)
    try:
        return send_file(filepath)
    except FileNotFoundError:
        return "File not found", 404

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/getSession')
def getSession():
    if 'user' in session:
        return jsonify({'user': session['user']})
    else:
        return jsonify({'user': None})

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/login')
def login():
    return render_template('login.html')

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/processLogin', methods=['POST'])
def processLogin():
    username = request.json['username']
    password = request.json['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        cursor.execute(f'''
            SELECT * FROM users WHERE username = '{username}' AND password = '{password}'
        ''')
    except:
        return jsonify({'status': 'failed'})
    
    user = cursor.fetchone()

    if user:
        session['user'] = user
        session['id'] = random.randint(0, 1000000000)
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failed'})
    
@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/logout')
def logout():
    session.pop('user', None)
    return redirect('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81')
    
@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/forum')
def forum():
    return render_template('forum.html')

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/forum/getPosts')
def getPosts():
    try:
        userID = session['id']
    except:
        return jsonify({'status': 'failed', 'message': 'You are not logged in!'})

    conn = sqlite3.connect(f'forum{userID}.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            poster TEXT,
            title TEXT UNIQUE,
            content TEXT
        )
    ''')

    cursor.execute('''
        SELECT * FROM posts
    ''')
    posts = cursor.fetchall()
    
    return jsonify({'status': 'success', 'posts': posts})

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/forum/makePost', methods=['POST'])
def makePost():
    try:
        userID = session['id']
        poster = session['user'][1]
        title = request.json['title']
        content = request.json['content']
    except:
        return jsonify({'status': 'failed', 'message': 'You are not logged in!'})

    try:
        with open(f'forum{userID}.db', 'r') as f:
            pass
    except FileNotFoundError:
        conn = sqlite3.connect(f'forum{userID}.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                poster TEXT,
                title TEXT UNIQUE,
                content TEXT
            )
        ''')

    conn = sqlite3.connect(f'forum{userID}.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM posts WHERE title = ?', (title,))
    isUniqueTitle = cursor.fetchone() == None
    if not isUniqueTitle:
        return jsonify({'status': 'failed', 'message': 'Post already exists!'})

    cursor.execute(f'''
        INSERT INTO posts (poster, title, content) VALUES (?, ?, ?)
    ''', (poster, title, content))
    conn.commit()

    return jsonify({'status': 'success'})

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/forum/allPosts')
def allPosts():
    return render_template('allPosts.html')

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/forum/getAllPosts')
def getAllPosts():
    if session['user'][1] != 'd82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892':   # not admin
        return jsonify({'status': 'failed', 'message': 'You are not an admin!'})

    files = os.listdir()
    files = [f for f in files if f.startswith('forum') and f.endswith('.db')]

    allPosts = []
    for f in files:
        conn = sqlite3.connect(f)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM posts')
        posts = cursor.fetchall()

        allPosts += posts
    
    return jsonify({'status': 'success', 'posts': allPosts})

if __name__ == '__main__':
    app.run(debug=True)

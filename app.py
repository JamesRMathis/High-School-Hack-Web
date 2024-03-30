from flask import Flask, render_template, send_from_directory, redirect, request, jsonify, session, send_file
import sqlite3
import random
import json
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

def checkBadSession():
    if 'user' in session:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute(f'''
            SELECT * FROM users WHERE username = ? AND password = ?
        ''', (session['user'][1], session['user'][2]))
        user = cursor.fetchone()
        if not user:
            session.pop('user', None)

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
    if not checkBadSession():
        return jsonify({'status': 'failed', 'message': 'You are not logged in!'})

    try:
        userID = session['id']
    except:
        return jsonify({'status': 'failed', 'message': 'You are not logged in!'})

    conn = sqlite3.connect('userData.db')
    cursor = conn.cursor()

    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS posts{userID} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            poster TEXT,
            title TEXT UNIQUE,
            content TEXT
        )
    ''')

    cursor.execute(f'''
        SELECT * FROM posts{userID}
    ''')
    posts = cursor.fetchall()
    
    return jsonify({'status': 'success', 'posts': posts})

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/forum/makePost', methods=['POST'])
def makePost():
    if not checkBadSession():
        return jsonify({'status': 'failed', 'message': 'You are not logged in!'})

    try:
        userID = session['id']
        poster = session['user'][1]
        title = request.json['title']
        content = request.json['content']
    except:
        return jsonify({'status': 'failed', 'message': 'You are not logged in!'})

    conn = sqlite3.connect('userData.db')
    cursor = conn.cursor()

    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS posts{userID} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            poster TEXT,
            title TEXT UNIQUE,
            content TEXT
        )
    ''')

    cursor.execute(f'SELECT * FROM posts{userID} WHERE title = ?', (title,))
    isUniqueTitle = cursor.fetchone() == None
    if not isUniqueTitle:
        return jsonify({'status': 'failed', 'message': 'Post already exists!'})

    cursor.execute(f'''
        INSERT INTO posts{userID} (poster, title, content) VALUES (?, ?, ?)
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

    conn = sqlite3.connect('userData.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    tables =  [table[0] for table in tables if table[0].startswith('posts')]

    for table in tables:
        cursor.execute(f'SELECT * FROM {table}')
        posts = cursor.fetchall()
        allPosts += posts
    
    return jsonify({'status': 'success', 'posts': allPosts})

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/account')
def account():
    return render_template('account.html')

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/account/postItem', methods=['POST'])
def addItem():
    if not checkBadSession():
        return jsonify({'status': 'failed', 'message': 'You are not logged in!'})

    try:
        userID = session['id']
        category = request.json['category']
        name = request.json['name']
        price = request.json['price']
    except:
        return jsonify({'status': 'failed', 'message': 'You are not logged in!'})
    
    conn = sqlite3.connect('userData.db')
    cursor = conn.cursor()

    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS items{userID} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            jsonObj TEXT
        )
    ''')

    itemObj = {
        f'{name}': price
    }

    cursor.execute(f'SELECT * FROM items{userID} WHERE category = ?', (category,))
    categoryExists = cursor.fetchone() != None

    if not categoryExists:
        jsonified = json.dumps(itemObj)
        cursor.execute(f'INSERT INTO items{userID} (category, jsonObj) VALUES (?, ?)', (category, jsonified))
    else:
        cursor.execute(f'SELECT jsonObj FROM items{userID} WHERE category = ?', (category,))
        existingObj = json.loads(cursor.fetchone()[0])
        existingObj.update(itemObj)
        jsonified = json.dumps(existingObj)
        cursor.execute(f'UPDATE items{userID} SET jsonObj = ? WHERE category = ?', (jsonified, category))
    conn.commit()

    return jsonify({'status': 'success'})

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/account/getItems')
def getItems():
    if not checkBadSession():
        return jsonify({'status': 'failed', 'message': 'You are not logged in!'})

    try:
        userID = session['id']
    except:
        return jsonify({'status': 'failed', 'message': 'You are not logged in!'})

    conn = sqlite3.connect('userData.db')
    cursor = conn.cursor()

    # every user should see all items across all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    tables =  [table[0] for table in tables if table[0].startswith('items')]
    allItems = {}
    for table in tables:
        cursor.execute(f'SELECT * FROM {table}')
        items = cursor.fetchall()
        for item in items:
            category = item[1]
            jsonObj = json.loads(item[2])
            if category not in allItems:
                allItems[category] = jsonObj
            else:
                allItems[category].update(jsonObj)
    
    return jsonify({'status': 'success', 'items': allItems})

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/adminPanel')
def adminPanel():
    if session['user'][1] != 'd82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892':
        return 'You are not an admin!'
    
@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/adminPanel/getUsers')
def getUsers():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return jsonify({'status': 'success', 'users': users})

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/adminPanel/removeUser', methods=['POST']) 
def removeUser():
    username = request.json['username']
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE username = ?', (username,))
    conn.commit()
    return jsonify({'status': 'success'})

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/adminPanel/confirmPassword', methods=['POST'])
def confirmPassword():
    password = request.json['password']
    if password == 'FLAG{DECODING_THE_COOKIE_AGAIN???}':
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failed'})

if __name__ == '__main__':
    app.run(debug=True)

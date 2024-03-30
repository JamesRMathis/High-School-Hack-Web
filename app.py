from flask import Flask, render_template, send_from_directory, redirect, request, jsonify, session, send_file, make_response
import sqlite3
import json
import base64

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

@app.route('/', methods=['GET'])
def index():
    cookie = base64.b64encode("FLAG{St4rG4z3rS3cr3t}".encode())
    resp = make_response(send_from_directory('static', 'gateway.html'))
    resp.set_cookie('cosmicKey', cookie, max_age=60*60*24*365)  # Example: 1 year
    resp.headers["Onetwo"] = "FLAG{Buckl3MySh03}"
    return resp

@app.route('/', methods=['POST'])
def index_post():
    return redirect('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a82', filename="index.html")

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
    
@app.route("/gateway")
def gateway():
    return jsonify({"url":"rocket.jpg","title":"Galactic Explorers' Rocket Compendium","name-1":"Arnav Mathis","name-2":"James Karekar","flag":"FLAG{UF0rG0tTh3D4t4}"})


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
        session['gss-member'] = False
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failed'})
    
@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/forum')
def forum():
    return render_template('forum.html')
@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81/account')
def account():
    return render_template('account.html')

@app.route('/getItems')
def getItems():
    return jsonify({"Weapons":{"gun":["100000000","arnav"],"pain":["1324029384","test"]}})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, send_from_directory, redirect, request, send_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'gateway.html')
    # return 'Hello, World!'

@app.route('/', methods=['POST'])
def index_post():
    return redirect('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81', filename="index.html")

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a83')
def login():
    return render_template('login.html')

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a82')
def haha():
    filename = request.args.get('filename')
    filepath = f"./static/{filename}"  # This is insecure!
    try:
        return send_file(filepath)
    except FileNotFoundError:
        return "File not found", 404

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

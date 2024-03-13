from flask import Flask, render_template, send_from_directory, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'gateway.html')
    # return 'Hello, World!'

@app.route('/', methods=['POST'])
def index_post():
    return redirect('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81')

@app.route('/bb170201ef5d8f4449fd06812f53dc3d970875ca2c25abbe2bfc3683db807a81')
def login():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import scripts.DBConn as db

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    print(db.ler_dados())
    return render_template('index.html')

@app.route('/login.html', methods=['GET'])
def sign_in():
    return render_template('login.html')

@app.route('/cadastro.html', methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        return render_template('cadastro.html')
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import scripts.Login as dbLogin

app = Flask(__name__)
app.secret_key = './cred/challenge-34b16-firebase-adminsdk-3f6qu-dadfc59fab.json'  # Necessário para usar flash messages

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/login.html', methods=["POST", "GET"])
def sign_in():
    print("login")
    print(request.method)
    if request.method == "GET":
        username = request.form.get("username")
        password = request.form.get("password")

        if dbLogin.verificar_login(username, password):
            return render_template('login.html')
        else:
            flash('Login falhou. Por favor, tente novamente.')

    return render_template('login.html')

@app.route('/cadastro.html', methods=['GET', 'POST'])
def sign_up():
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)
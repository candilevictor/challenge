import firebase_admin
from firebase_admin import credentials, db

# Verifica se o Firebase já foi inicializado
if not firebase_admin._apps:
    cred = credentials.Certificate("challenge\cred\challenge-34b16-firebase-adminsdk-3f6qu-3403a911e7.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://challenge-34b16-default-rtdb.firebaseio.com"
    })

# Escrevendo dados
ref = db.reference('/Main')
ref.set({
    "usuario": {
        "email": "admin1@gmail.com",
        "senha": "123ABC+"
    }
})

#Lendo dados
ref = db.reference('/Main')
dados = ref.get()
print(dados)

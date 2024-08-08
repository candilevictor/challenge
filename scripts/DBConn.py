import firebase_admin
from firebase_admin import credentials, db

# Verifica se o Firebase já foi inicializado
if not firebase_admin._apps:
    cred = credentials.Certificate("./cred/challenge-34b16-firebase-adminsdk-3f6qu-dadfc59fab.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://challenge-34b16-default-rtdb.firebaseio.com"
    })

def Escrever_dado(valor):
    # Escrevendo dados
    ref = db.reference('/Main')
    ref.set({valor})

def ler_dados():
    #Lendo dados
    ref = db.reference('/Main')
    dados = ref.get()
    return dados

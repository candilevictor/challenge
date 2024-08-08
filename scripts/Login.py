import scripts.DBConn as Conn

def verificar_login(usuario, senha):
    print("verificando login")
    dados = Conn.ler_dados()

    if dados:
        for key, value in dados.items():
            if value.get('usuario') == usuario and value.get('senha') == senha:
                return True
    return False

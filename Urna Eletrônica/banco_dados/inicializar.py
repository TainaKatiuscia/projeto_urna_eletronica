from banco_dados.conexao import obter_conexao

def criar_tabelas():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        votos INTEGER DEFAULT 0
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS eleitores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf TEXT UNIQUE NOT NULL,
        nome TEXT NOT NULL,
        votou INTEGER DEFAULT 0
    )
    """)
    conexao.commit()
    conexao.close()

def cadastrar_candidatos():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    candidatos = [
        "José Luiz Datena",
        "Pablo Marçal",
        "Tabata Amaral",
        "Guilherme Boulos",
        "Ricardo Nunes",
        "Nulo",
        "Branco"
    ]
    for nome in candidatos:
        cursor.execute("INSERT OR IGNORE INTO candidatos (nome) VALUES (?)", (nome,))
    conexao.commit()
    conexao.close()

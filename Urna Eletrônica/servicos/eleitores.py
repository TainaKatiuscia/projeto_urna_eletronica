from banco_dados.conexao import obter_conexao

def registrar_eleitor():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    print("\n--- Registrar Eleitor ---")
    cpf = input("Digite o CPF do eleitor: ")
    nome = input("Digite o nome completo do eleitor: ")
    try:
        cursor.execute("INSERT INTO eleitores (cpf, nome) VALUES (?, ?)", (cpf, nome))
        conexao.commit()
        print("Eleitor registrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: CPF já está registrado no sistema.")
    conexao.close()

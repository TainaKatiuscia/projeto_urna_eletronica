from banco_dados.conexao import obter_conexao

def votar():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    print("\n--- Votação ---")
    cpf = input("Digite o CPF do eleitor: ")

    cursor.execute("SELECT id, votou FROM eleitores WHERE cpf = ?", (cpf,))
    eleitor = cursor.fetchone()

    if not eleitor:
        print("Erro: CPF não encontrado. Registre o eleitor antes de votar.")
        return
    if eleitor[1] == 1:
        print("Erro: Este eleitor já votou.")
        return

    print("\nCandidatos:")
    cursor.execute("SELECT id, nome FROM candidatos ORDER BY id")
    candidatos = cursor.fetchall()
    for candidato in candidatos:
        print(f"{candidato[0]} - {candidato[1]}")

    try:
        voto = int(input("Digite o número do candidato ou escolha [6 para Nulo, 7 para Branco]: "))
        cursor.execute("UPDATE candidatos SET votos = votos + 1 WHERE id = ?", (voto,))
        cursor.execute("UPDATE eleitores SET votou = 1 WHERE id = ?", (eleitor[0],))
        conexao.commit()
        print("Voto registrado com sucesso!")
    except ValueError:
        print("Erro: Digite um número válido.")
    except sqlite3.IntegrityError:
        print("Erro: Candidato inválido.")
    conexao.close()

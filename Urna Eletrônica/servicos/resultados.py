from banco_dados.conexao import obter_conexao

def exibir_resultados():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    print("\n--- Resultado da Eleição ---")
    cursor.execute("SELECT nome, votos FROM candidatos ORDER BY votos DESC")
    resultados = cursor.fetchall()
    for nome, votos in resultados:
        print(f"{nome}: {votos} votos")
    conexao.close()

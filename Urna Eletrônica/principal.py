from banco_dados.inicializar import criar_tabelas, cadastrar_candidatos
from servicos.eleitores import registrar_eleitor
from servicos.votacao import votar
from servicos.resultados import exibir_resultados

def menu():
    while True:
        print("\n--- Sistema de Urna Eletrônica ---")
        print("1. Registrar Eleitor")
        print("2. Votar")
        print("3. Exibir Resultados")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            registrar_eleitor()
        elif escolha == "2":
            votar()
        elif escolha == "3":
            exibir_resultados()
        elif escolha == "4":
            print("Encerrando o sistema. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    criar_tabelas()
    cadastrar_candidatos()
    menu()

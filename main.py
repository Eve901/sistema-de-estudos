import json

tarefas = []

def salvar_tarefas():
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)


def carregar_tarefas():
    global tarefas

    try:
        with open("tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)
    except:
        tarefas = []
        
def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    prazo = input("Digite o prazo: ")

    tarefa = {
        "nome": nome,
        "prazo": prazo,
        "concluida": False
    }

    tarefas.append(tarefa)
    salvar_tarefas()
    print("Tarefa adicionada com sucesso!\n")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return

    for i, tarefa in enumerate(tarefas):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i} - {tarefa['nome']} | Prazo: {tarefa['prazo']} | {status}")
    print()

def concluir_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa concluída: "))

        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            salvar_tarefas()
            print("Tarefa marcada como concluída!\n")
        else:
            print("Índice inválido!\n")

    except:
        print("Por favor, digite um número válido!\n")

def menu():
    while True:
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Deletar tarefa")
        print("5 - Editar tarefa")
        print("6 - Sair")
        

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            deletar_tarefa()
        elif opcao == "5":
            editar_tarefa()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

def deletar_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa que deseja deletar: "))

        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            salvar_tarefas()
            print("Tarefa deletada com sucesso!\n")
        else:
            print("Índice inválido!\n")

    except:
        print("Digite um número válido!\n")

def editar_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa que deseja editar: "))

        if 0 <= indice < len(tarefas):
            novo_nome = input("Digite o novo nome da tarefa: ")
            novo_prazo = input("Digite o novo prazo: ")

            tarefas[indice]["nome"] = novo_nome
            tarefas[indice]["prazo"] = novo_prazo

            salvar_tarefas()
            print("Tarefa atualizada com sucesso!\n")
        else:
            print("Índice inválido!\n")

    except:
        print("Digite um número válido!\n")

carregar_tarefas()
menu()


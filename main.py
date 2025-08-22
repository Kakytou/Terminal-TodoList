import json
from time import sleep

tarefas = []

def carregar_tarefas():
    global tarefas
    try:
        with open("tarefas.json", "r",encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []

def adicionar_tarefa():
    nome_tarefa = input("Digite o nome da tarefa: ").lower()
    data_limite = input("Deseja inserir uma data de conclusão (s/n)? ").lower()
    if data_limite == "s":
        data_limite = input("Digite em que dia e mês será a conclusão: ")
        tarefas.append({"Tarefa":nome_tarefa, "Data conclusao":data_limite})
    else:
        tarefas.append({"Tarefa":nome_tarefa})

def mostrar_tarefa():
    if tarefas:
        for tarefa in tarefas:
            if "Data conclusao" in tarefa and "Conclusao" in tarefa:
                print(f"A tarefa: {tarefa['Tarefa']}, Data de conclusão: {tarefa['Data conclusao']}, Status: {tarefa['Conclusao']} ")
            elif "Data conclusao" in tarefa:
                print(f"A tarefa: {tarefa['Tarefa']}, Data de conclusão: {tarefa['Data conclusao']} ")
            elif "Conclusao" in tarefa:
                print(f"A tarefa: {tarefa['Tarefa']}, Status: {tarefa['Conclusao']}")
            else:
                print(f"A tarefa: {tarefa['Tarefa']}")
    else:
        print("Nenhuma tarefa existente.")

def concluir_tarefa():
    if tarefas:
        concluir_tarefa = input("Digite a tarefa que deseja concluir: ").strip().lower()
        for tarefa in tarefas:
            if tarefa["Tarefa"] == concluir_tarefa:
                tarefa.update(Conclusao = "Concluído")
                print(f"Tarefa: {tarefa['Tarefa']}, Status: {tarefa['Conclusao']}")
    else:
        print("Nenhuma tarefa existente.")

def deletar_tarefa():
    if tarefas:
        tarefa_removida = input("Digite o nome da tarefa para remover: ").strip().lower()
        for remover_tarefa in tarefas:
            if "Data conclusao" in remover_tarefa:
                if remover_tarefa["Tarefa"] == tarefa_removida:
                    tarefas.remove(remover_tarefa)
                    print("Tarefa e data removidas!")
            elif remover_tarefa["Tarefa"] == tarefa_removida:
                tarefas.remove(remover_tarefa)
                print("Tarefa Removida!")
    else:
        print("Nenhuma tarefa existente.")

def menu():
    carregar_tarefas()
    
    while True:
        
        print("\n1. Adicionar tarefa")
        print("2. Mostrar tarefas")
        print("3. Concluir tarefa")
        print("4. Deletar tarefa")
        print("5. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            mostrar_tarefa()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            deletar_tarefa()
        elif opcao == "5":
            print("Saindo e salvando...")
            with open("tarefas.json","w", encoding="utf-8") as arquivo:
                json.dump(tarefas,arquivo,indent=4,ensure_ascii=False)
            sleep(1)
            break
        else:
            print("Digite uma opção válida!")
            
if __name__ == "__main__":
    menu()
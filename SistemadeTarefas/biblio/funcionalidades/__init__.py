from SistemadeTarefas.biblio.interface import *

tarefas = {}

def cadastrar_tarefa():
    id_tarefa = len(tarefas) + 1
    descricao = input("Digite a descrição da tarefa: ")
    data_criacao = input("Digite a data de criação da tarefa (DD/MM/YYYY): ")
    data_conclusao = "Não concluída"
    status = "pendente"
    tarefa = {"descricao": descricao, "data_criacao": data_criacao, "data_conclusao": data_conclusao, "status": status}
    tarefas[id_tarefa] = tarefa
    cabecalho("Tarefa cadastrada com sucesso!")

# def listar_tarefas():
#     if len(tarefas) == 0:
#         print("Não há tarefas cadastradas.")
#     else:
#         for id_tarefa, tarefa in tarefas.items():
#             print(f"ID: {id_tarefa} | Descrição: {tarefa['descricao']} | Data de criação: {tarefa['data_criacao']}"
#                   f" | Data de conclusão: {tarefa['data_conclusao']} | Status: {tarefa['status']}")
# def listar_tarefas():
#     if len(tarefas) == 0:
#         print("Não há tarefas cadastradas.")
#     else:
#         print(f"{'ID':<5} {'Descrição':<30} {'Data de criação':<20} {'Data de conclusão':<20} {'Status':<10}")
#         print("="*85)
#         for id_tarefa, tarefa in tarefas.items():
#             print(f"{id_tarefa:<5} {tarefa['descricao']:<30} {tarefa['data_criacao']:<20} {tarefa['data_conclusao']:<20} {tarefa['status']:<10}")
#         print("="*85)
def listar_tarefas():
    if len(tarefas) == 0:
        print("{:*^85s}".format("Não há tarefas cadastradas."))
    else:
        print("{:*^85s}".format(" Lista de Tarefas "))
        print("{:<5s} {:<30s} {:<20s} {:<20s} {:<15s}".format("ID", "Descrição", "Data de Criação", "Data de Conclusão", "Status"))

        for id_tarefa, tarefa in tarefas.items():
            print("{:<5s} {:<30s} {:<20s} {:<20s} {:<15s}".format(str(id_tarefa), tarefa["descricao"], tarefa["data_criacao"], tarefa["data_conclusao"], tarefa["status"]))

        print("{:*^85s}".format(""))


def editar_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa que deseja editar: "))
    if id_tarefa not in tarefas:
        print("Tarefa não encontrada.")
    else:
        tarefa = tarefas[id_tarefa]
        print("Digite os novos dados da tarefa:")
        descricao = input(f"Descrição ({tarefa['descricao']}): ")
        data_criacao = input(f"Data de criação ({tarefa['data_criacao']}): ")
        data_conclusao = input(f"Data de conclusão ({tarefa['data_conclusao']}): ")
        status = input(f"Status ({tarefa['status']}): ")
        if descricao != "":
            tarefa['descricao'] = descricao
        if data_criacao != "":
            tarefa['data_criacao'] = data_criacao
        if data_conclusao != "":
            tarefa['data_conclusao'] = data_conclusao
        if status != "":
            tarefa['status'] = status
        tarefas[id_tarefa] = tarefa
        cabecalho("Tarefa editada com sucesso!")

def excluir_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa que deseja excluir: "))
    if id_tarefa not in tarefas:
        print("Tarefa não encontrada.")
    else:
        del tarefas[id_tarefa]
        cabecalho("Tarefa excluída com sucesso!")

def relatorio_tarefas_concluidas():
    concluidas = [tarefa for tarefa in tarefas.values() if tarefa['status'] == 'concluída']
    if len(concluidas) == 0:
        print("Não há tarefas concluídas.")
    else:
        cabecalho("Tarefas concluídas:")
        for tarefa in concluidas:
            print(f"- {tarefa['descricao']} ({tarefa['data_conclusao']})")

def pesquisar_tarefas():
    palavra_chave = input("Digite uma palavra-chave para pesquisa: ")
    encontradas = [tarefa for tarefa in tarefas.values() if palavra_chave in tarefa['descricao']]
    if len(encontradas) == 0:
        print("Nenhuma tarefa encontrada.")
    else:
        print(f"Tarefas encontradas ({len(encontradas)}):")
        for tarefa in encontradas:
            print(f"- {tarefa['descricao']} ({tarefa['data_criacao']})")

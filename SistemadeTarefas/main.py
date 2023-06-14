from SistemadeTarefas.biblio.funcionalidades import *
from SistemadeTarefas.biblio.interface import *

def main():
  tarefas = []
  while True:
    resposta = exibirMenu(['Opção - Cadastrar', 'Opção - Listar tarefa(s)','Opção - Editar tarefa(s)',
                           'Opção - Excluir tarefa(s)', 'Opção - Relatorio de tarefa(s) concluidas',
                           'Opção - Pesquisar tarefa(s)', 'Opção - Sair'])
    if resposta == 1:
      cabecalho('Novo cadastro')
      cadastrar_tarefa()

    elif resposta == 2:
      cabecalho('Listar tarefa(s)')
      listar_tarefas()

    elif resposta == 3:
      cabecalho('Editar tarefa(s)')
      editar_tarefa()

    elif resposta == 4:
      cabecalho('Excluir tarefa(s)')
      excluir_tarefa()

    elif resposta == 5:
      cabecalho('Relatorio de tarefa(s)')
      relatorio_tarefas_concluidas()

    elif resposta == 6:
      cabecalho('Pesquisar tarefa(s)')
      pesquisar_tarefas()

    elif resposta == 7:
      cabecalho('Saindo do programa, até logo!!!')
      break

if __name__ == '__main__':
    main()
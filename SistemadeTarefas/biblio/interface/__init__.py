def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(' ERRO: por favor, digite a opção válida. ')
            continue
        except KeyboardInterrupt:
            print(' Usuário preferiou não digitar a opção. ')
            return 0
        else:
            return n

def linha(tam=42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def exibirMenu(lista):
    cabecalho('Sistema de Tarefas ')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    opcao=leiaInt('Sua Opção: ')
    return opcao
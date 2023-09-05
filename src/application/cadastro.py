# projeto devops
# cadastros de e-mail
# permitir visualizar todos os e-mails cadastrados no banco de dados

def menu():
    opcao=input('Bem-vindo!\nEscolha uma opção:\n1-Cadastrar e-mail\n2-Listar e-mails cadastrados\n3-Sair\n')
    return int(opcao)


while True:
    opcao = menu()
    if opcao == 1:
        print("Cadastrar e-mail!")
    elif opcao == 2:
        print("Listar e-mails!")
    else:
        print("Saindo...")
        break

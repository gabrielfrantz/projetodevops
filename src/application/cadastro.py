# projeto devops
# cadastros de e-mail
# permitir visualizar todos os e-mails cadastrados no banco de dados

import psycopg2

def menu(): #menu mostrado para o usuário realizar uma ação
    opcao=input("Bem-vindo!\nEscolha uma opção:\n1-Cadastrar e-mail\n2-Listar e-mails cadastrados\n3-Sair\n")
    return int(opcao)

def conectadb(): #conexao com o banco de dados postgres
    conexao = psycopg2.connect(host="localhost",
                               database="cadastros",
                               user="postgres",
                               password="postgres",
                               port=5000)
    return conexao

def sqlCadastro(email): #sql para cadastro
    conexao = conectadb()
    cursor = conexao.cursor()
    try:
        sql = 'INSERT INTO tabela VALUES (DEFAULT,\'{}\')'.format(email)
        cursor.execute(sql)
        conexao.commit()
        print("Cadastro de e-mail realizado com sucesso!\n")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro ao cadastrar o e-mail desejado!\n", error)
        conexao.rollback()
        cursor.close()
        return 1

def sqlListagem(): #sql para listagem
    conexao = conectadb()
    cursor = conexao.cursor()
    try:
        sql = f'SELECT * FROM tabela;'
        cursor.execute(sql)
        print("Listando os e-mails cadastrados!\n")
        dados = cursor.fetchall()
        registros = []
        for i in dados:
            registros.append(i)
            print(i)
        cursor.close()
        print("\n")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erro ao listar os e-mails cadastrados!\n", error)
        cursor.close()
        return 1    

while True: #loop do menu para o usuário escolher uma ação correta
    opcao = menu()
    if opcao == 1:
        email=input("Digite o e-mail a ser cadastrado: ")
        sqlCadastro(email)
    elif opcao == 2:
        sqlListagem()
    elif opcao == 3:
        print("Saindo!\n")
        break
    else:
        print("Opção incorreta, por favor, escolha uma opção do menu!")

"""
Faça um programa para gerenciar uma agenda de contatos. Para cada contato
armazene o nome, o telefone e o aniversário (dia e mês). O programa deve permitir.

(a) inserir contato
(b) remover contato
(c) pesquisar um contato pelo nome
(d) listar todos os contatos
(e) listar os contatos cujo nome inicia com uma dada letra
(f) imprimir os aniversariantes do mês.

Sempre que o programa for encerrado, os contatos devem ser armazenados em um
arquivo binário. Quando o programa iniciar, os contatos devem ser inicializados
com os dados contidos neste arquivo binário.

Passos
(a) inserir contato
    contato deve ter:
        -> nome
        -> telefone
        -> aniversário (dia e mês)

(b) remover contato
    -> Para remover tem que inserir o nome do contato
(c) pesquisar um contato pelo nome
    -> Se tiver o contato retornar os dados
    -> Se não relatar "USER NOT FOUND"
(d) listar todos os contatos
(e) listar os contatos cujo nome inicia com uma dada letra
(f) imprimir os aniversariantes do mês.

"""


def inserir_contato():
    name = input('Enter the name: ').title()
    tel = input('Enter the number of telefone: ')
    birth = input('Enter the birthday: ')
    with open('contatos.txt', 'a') as arq:
        arq.write(f'Name: {name} | Telephone: {tel} | BirthDay: {birth}\n')
    return 'Add with sucess'


def get_name(contato):
    name = contato[contato.index(':') + 1: contato.index('|')].strip()
    return name.lower()


def remover_contato(name):
    with open('contatos.txt', 'r') as arq:
        lista_de_contatos = arq.readlines()
        nova_lista_de_contatos = []
        for contato in lista_de_contatos:
            if name.lower().strip() == get_name(contato):
                pass
            else:
                nova_lista_de_contatos.append(contato)
    with open('contatos.txt', 'w') as arq:
        arq.writelines(nova_lista_de_contatos)
    return 'Drop User with sucess'


def pesquisa_contato(name):
    with open('contatos.txt', 'r') as arq:
        lista_de_contatos = arq.readlines()
        encontrado = 0
        for contato in lista_de_contatos:
            if name.lower().strip() == get_name(contato):
                return contato
        if not encontrado:
            return 'User not found'


def listando_todos_contatos():
    with open('contatos.txt', 'r') as arq:
        lista_de_contatos = arq.readlines()
        print("-" * 20 + ' Lista de Contatos ' + "-" * 20)
        for contato in lista_de_contatos:
            print(contato, end='')
        print('-' * 59)


def listar_nome_com_dada_letra(name):
    with open('contatos.txt', 'r') as arq:
        lista_de_contatos = arq.readlines()
        print("-" * 20 + " Possibles Contacts " + "-" * 20)
        for contato in lista_de_contatos:
            if name.lower() in get_name(contato):
                print(contato, end='')
        print('-' * 60)


def get_mouth(contato):
    p1 = contato[::-1]
    p2 = p1[:p1.index(':')].strip()
    p3 = p2[::-1]
    month = p3[p3.index('/') + 1:]
    return int(month)


def current_month():
    from datetime import date
    month = date.today().month
    return int(month)


def lista_de_aniversariante_do_mes():
    with open('contatos.txt', 'r') as arq:
        lista_de_contatos = arq.readlines()
        print('-' * 10 + ' Lista de Aniversariantes do Mês ' + '-' * 10)
        for contato in lista_de_contatos:
            if get_mouth(contato) == current_month():
                print(contato, end='')
        print('-' * 53)


def apresentacao():
    print("""Agenda de Contatos
    Opções: 
    1 - Inserir contato
    2 - Remover contato
    3 - Pesquisar porcontato pelo nome
    4 - Para listar todos os contatos
    5 - Para listar os contatos cujo nome inicia com uma dada letra
    6 - imprimir os aniversariantes do mês
    7 - Sair
    """)


def clean():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


# Rotina Principal ---------------------------------------
while True:
    try:
        from time import sleep
        clean()
        apresentacao()
        op = int(input('Insira a opção: '))
        if op == 1:
            inserir_contato()
        elif op == 2:
            nome = input('Insira um nome: ')
            print(remover_contato(nome))
        elif op == 3:
            nome = input('Insira um nome: ')
            print(pesquisa_contato(nome))
        elif op == 4:
            listando_todos_contatos()
        elif op == 5:
            nome = input('Insira um nome: ')
            listar_nome_com_dada_letra(nome)
        elif op == 6:
            lista_de_aniversariante_do_mes()
        elif op == 7:
            break
        else:
            print('Opção Errada')
        sleep(2)
    except ValueError as err:
        from time import sleep
        print(f"Erro: {err}")
        sleep(2)


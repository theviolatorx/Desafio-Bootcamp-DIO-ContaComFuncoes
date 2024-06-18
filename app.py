import os

menuCliente = """
#####################################################

MENU CLIENTE

[ C ] - Criar Usuário
[ L ] - Logar Usuário
[ Q ] - Sair

#####################################################

Escolha a sua opção:
"""

menuContas = """
#####################################################

MENU CONTAS

[ C ] - Criar Contas
[ L ] - Logar Contas
[ I ] - Inativar Contas
[ Q ] - Retornar Menu Anterior

#####################################################

Escolha a sua opção:
"""

menuOperacoes = """
#####################################################
# Agência: 0001 - Conta: xxxx -                     #
# CPF: xxxxxxxxxxx - Nome: yyyyyyy yyyyyyyy yyy     #
#####################################################

ESCOLHA A OPERAÇÃO:

[ D ] - Depósito
[ S ] - Saque
[ E ] - Extrato
[ Q ] - Retornar Menu Anterior

#####################################################

Escolha a sua opção:
"""
clientes = {
    "11111111111": {
        "nome": "Paulo Ambrosio",
        "datanascimento": "15/06/1975",
        "endereco": {
            "logradouro": "Av. Brasil",
            "nro": 234,
            "bairro": "Vila Nova Itanhaém",
            "cidade": "Itanhaém",
            "uf": "SP"
        },
        "contas": {
            "id": None
        },
        "situacao": "A",
        "logado": False
    },
    "22222222222": {
        "nome": "Ana Pereira",
        "datanascimento": "15/03/1980",
        "endereco": {
            "logradouro": "Rua A",
            "nro": 101,
            "bairro": "Centro",
            "cidade": "São Paulo",
            "uf": "SP"
        },
        "contas": {
            "id": None
        },
        "situacao": "A",
        "logado": False
    },
    "33333333333": {
        "nome": "Bruno Silva",
        "datanascimento": "22/07/1992",
        "endereco": {
            "logradouro": "Rua B",
            "nro": 202,
            "bairro": "Vila Nova",
            "cidade": "Rio de Janeiro",
            "uf": "RJ"
        },
        "contas": {
            "id": None
        },
        "situacao": "A",
        "logado": False
    },
    "44444444444": {
        "nome": "Carlos Souza",
        "datanascimento": "10/11/1985",
        "endereco": {
            "logradouro": "Rua C",
            "nro": 303,
            "bairro": "Jardim América",
            "cidade": "Belo Horizonte",
            "uf": "MG"
        },
        "contas": {
            "id": None
        },
        "situacao": "A",
        "logado": False
    },
    "55555555555": {
        "nome": "Daniela Santos",
        "datanascimento": "05/05/1978",
        "endereco": {
            "logradouro": "Rua D",
            "nro": 404,
            "bairro": "Centro",
            "cidade": "Curitiba",
            "uf": "PR"
        },
        "contas": {
            "id": None
        },
        "situacao": "A",
        "logado": False
    },
    "66666666666": {
        "nome": "Eduardo Lima",
        "datanascimento": "30/09/1990",
        "endereco": {
            "logradouro": "Rua E",
            "nro": 505,
            "bairro": "São Francisco",
            "cidade": "Porto Alegre",
            "uf": "RS"
        },
        "contas": {
            "id": None
        },
        "situacao": "A",
        "logado": False
    },
    "77777777777": {
        "nome": "Fernanda Oliveira",
        "datanascimento": "14/02/1988",
        "endereco": {
            "logradouro": "Rua F",
            "nro": 606,
            "bairro": "Boa Vista",
            "cidade": "Salvador",
            "uf": "BA"
        },
        "contas": {
            "id": None
        },
        "situacao": "A",
        "logado": False
    },
    "88888888888": {
        "nome": "Gabriel Fernandes",
        "datanascimento": "25/12/1995",
        "endereco": {
            "logradouro": "Rua G",
            "nro": 707,
            "bairro": "Centro",
            "cidade": "Recife",
            "uf": "PE"
        },
        "contas": {
            "id": None
        },
        "situacao": "A",
        "logado": False
    },
    "99999999999": {
        "nome": "Helena Costa",
        "datanascimento": "08/08/1983",
        "endereco": {
            "logradouro": "Rua H",
            "nro": 808,
            "bairro": "Jardim Paulista",
            "cidade": "São Paulo",
            "uf": "SP"
        },
        "contas": {
            "id": None
        },
        "situacao": "A",
        "logado": False
    },
    "00000000000": {
        "nome": "Igor Martins",
        "datanascimento": "12/06/1987",
        "endereco": {
            "logradouro": "Rua I",
            "nro": 909,
            "bairro": "Santa Cecília",
            "cidade": "Fortaleza",
            "uf": "CE"
        },
        "contas": {
            "id": None
        },
        "situacao": "A",
        "logado": False
    },
    "11111111110": {
        "nome": "Juliana Alves",
        "datanascimento": "20/10/1993",
        "endereco": {
            "logradouro": "Rua J",
            "nro": 1010,
            "bairro": "Centro",
            "cidade": "Manaus",
            "uf": "AM"
        },
        "contas": {
            "id": None
        },
        "situacao": "A",
        "logado": False
    }
}


contas = {
    "conta": {
        "agencia": "001",
        "cliente": None,
        "saldo": None,
        "extrato": "\n",
        "limite_saque": 0,
        "situacao": None
    }
}

numero_conta = 1
clienteLogado = {}

saldo = 0
extrato = "\n"
saques_realizados = 0
LIMITE_SAQUE = 500
LIMITES_SAQUE_DIARIO = 3


def cliente(opMenu, clientes):
    os.system("cls")
    if (opMenu == 'c'):
        print("#####################################################")
        print("Cadastro de Cliente")
        print("#####################################################")
        print()
        while True:
            print("Informe o CPF do Cliente (sem pontos e sem digitos. Somente números):")
            cpf = input()
            if (cpf.isnumeric() and len(cpf) == 11):
                for chave in clientes:
                    if (chave == cpf):
                        print("CPF já cadastrado! Por favor, logue-se!")
                        return "", {}
                print("Informe o nome do Cliente: ")
                nome = input()
                print("Informe a data de nascimento do Cliente (dd/mm/aaaa):")
                datanascimento = input()
                print("Informe o nome da rua/avenida do Cliente: ")
                logradouro = input()
                print(
                    "Informe o número da casa: (Use s/n caso não tenha número) ")
                nro = input()
                print("Informe o bairro: ")
                bairro = input()
                print("Informe a cidade: ")
                cidade = input()
                print("Informe o UF: (Apenas a Sigla) ")
                uf = input()

                dadosClientes = {
                    "nome": nome,
                    "datanascimento": datanascimento,
                    "endereco": {
                        "logradouro": logradouro,
                        "nro": nro,
                        "bairro": bairro,
                        "cidade": cidade,
                        "uf": uf
                    },
                    "contas": {
                        "id": None
                    },
                    "situacao": "A",
                    "logado": False
                }

                return cpf, dadosClientes
            else:
                print("CPF inválido! CPF deve ter com 11 dígitos!")

    elif (opMenu == 'l'):
        print("#####################################################")
        print("# Login")
        print("#####################################################")
        print()
        while True:
            print(
                "Informe o CPF do Cliente (sem pontos e sem digitos. Somente números):")
            cpf = input()
            if (cpf.isnumeric() and len(cpf) == 11):
                for chave in clientes:
                    if (chave == cpf):
                        return cpf, {}
                print("CPF não localizado! Por favor, cadastre-se!")
                return "", {}
            else:
                print("CPF inválido! CPF deve ter com 11 dígitos!")


def conta():
    pass


def saques():
    pass


def deposito():
    pass


def extrato():
    pass


logado = False

while True:
    os.system("cls")
    print(menuCliente)
    opcao = input()
    print()

    if (opcao.lower() == 'c'):
        cpf, dadosClientes = cliente(opcao, clientes)
        if (cpf != ""):
            clientes[cpf] = dadosClientes
            print(clientes)
    elif (opcao.lower() == 'l'):
        cpf, _ = cliente(opcao, clientes)
        if (cpf != ""):
            clientes[cpf]["logado"] = True
            while clientes[cpf]["logado"]:
                os.system("cls")
                print(menuContas)
                opcao = input()
                print()
                if (opcao.lower() == 'c'):
                    pass
                elif (opcao.lower() == 'l'):
                    pass
                elif (opcao.lower() == 'i'):
                    pass
                elif (opcao.lower() == 'q'):
                    pass

    elif (opcao.lower() == "q"):
        os.system("cls")
        print("Obrigado por utilizar o nosso banco!")
        break
    else:
        print("Opção inválida!")
        continue

    print()
    if (not logado):
        print("Precione qualquer [ENTER] para retornar ao menu principal!")
        opcao = input()
    else:
        print("Ta logado!")
        pass

    """
    if (opcao.lower() == "s"):
        print("Informe o valor a ser depositado: ")
        valor_deposito = input()
        if (valor_deposito.isnumeric() and float(valor_deposito) > 0):
            valor_deposito = float(valor_deposito)
            saldo += valor_deposito
            print("Deposito realizado com sucesso!")
            extrato += f'Deposito R$  {valor_deposito:.2f}\n'
            extrato += f'Saldo    R$  {saldo:.2f}\n'
        else:
            print("Valor informado inválido!")
    elif (opcao.lower() == "s"):
        if (saques_realizados < LIMITES_SAQUE_DIARIO):
            print("Informe o valor a ser sacado: ")
            valor_saque = input()
            if (valor_saque.isnumeric() and float(valor_saque) > 0):
                valor_saque = float(valor_saque)
                if (valor_saque > LIMITE_SAQUE):
                    print(f'Valor de saque excedeu o valor de R$ {
                        LIMITE_SAQUE:.2f}!')
                elif (valor_saque > saldo):
                    print(f'Valor de saque excedeu o saldo em conta!')
                else:
                    saldo -= valor_saque
                    print("Saque realizado com sucesso!")
                    saques_realizados += 1
                    extrato += f'Saque    R$ -{valor_saque:.2f}\n'
                    extrato += f'Saldo    R$  {saldo:.2f}\n'
            else:
                print("Valor informado inválido!")
        else:
            print(f'Você já excedeu o limite de saques diários! {
                  LIMITES_SAQUE_DIARIO} por dia!')
    elif (opcao.lower() == "e"):
        print("EXTRATO")
        print(extrato)
        print()
    elif (opcao.lower() == "q"):
        print("Obrigado por utilizar o nosso banco!")
        break
    else:
        print("Opção inválida!")
    """

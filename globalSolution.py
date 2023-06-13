#A função disponibiliza um menu onde o usuário pode escolher como irá se casdastrar (Pessoa Fisica ou Juridica)
def menu_cadastro():
    escolha = int(input('''
*_*==========================COMO DESEJA SE CADASTRAR====================================*_*
        Digite (1) para Pessoa Fisica
        Digite (2) para pessoas Juridica
*_*======================================================================================*_*
'''))
    return escolha
#A função cadastro tem os campos onde o usuário deve informar os dados necessários
def cadastro(escolha):
    pessoa = []
    match escolha:
        case 1: 
            nome = input("Informe seu nome: ")
            pessoa.append(nome)
            cpf = int(input("Informe seu cpf: "))
            pessoa.append(cpf)
            nacionalidade = input("Informe sua nacionalidade: ")
            pessoa.append(nacionalidade)
            return pessoa
        case 2:
            RazaoSocial = input("Informe a Razão Social: ")
            pessoa.append(RazaoSocial)
            cnpj = int(input("Informe o cnpj: "))
            pessoa.append(cnpj)
            nac = input("Informe a nacionalidade: ")
            pessoa.append(nac)
            return pessoa
#A função irá exibir um menu para que o usuário tire suas dúvidas caso tenha
def menu_info():
    duvida = "sim"
    while duvida == "sim" or duvida == "s":
        informacao = int(input('''
*_*===========================TEM ALGUMA DÚVIDA? ===================================*_*
            Digite (1) Para saber mais sobre nosso projeto
            Digite (2) Caso queira saber algumas informações sobre a fome 
            Digite (3) Caso tenha dúvida sobre a compra de moedas
            Digite (4) Para duvidas sobre doações
            Digite (0) caso não tenha dúvidas
*_*================================================================================*_*
        '''))
        match informacao:
            case 1: 
                print('''
                Nosso projeto se resume a uma aplicação que facilitaria a comunicação entre doadores e ONGs, 
                ele conta com um feed e uma área em que o usuário montará cestas de doações. 
                Isso melhora o processo de doação e potencializa o combate a fome no planeta.''')

                duvida = input("\nTem mais alguma dúvida? ")
            case 2: 
                print('''
                A fome é um problema global que afeta milhões de pessoas em todo o mundo. 
                Segundo a Organização das Nações Unidas para a Alimentação e Agricultura (FAO), 
                cerca de 828 milhões de pessoas foram afetadas pela fome em 2021, 
                enquanto 2,3 bilhões de pessoas sofrem de insegurança alimentar moderada ou grave em 2021.''')
                duvida = input("Tem mais alguma dúvida? ")
            case 3:
                print('''
                A compra de moedas é dentro do nosso app de forma simples e fácil, 
                primeiramente você deve informar a quantidade, logo em seguida escolher a forma de pagamento 
                após a compra ser aprovada as moedas estarão disponíveis na sua conta para que possa 
                realizar as doações.''')
                duvida = input("Tem mais alguma dúvida? ")
            case 4:
                print('''
                Para realizar uma doação no nosso app, 
                é necessário comprar moedas dentro do aplicativo trocando as por alimentos disponíveis 
                nos comércios cadastrado e selecinado a ONG que deseja doar.''')
                duvida = input("Tem mais alguma dúvida? ")
            case 0:
                print("Ok, vamos para o proximo passo")
                break
            case _:
                print("NUMERO INVALIDO!!!")
                duvida = input("Deseja digitar novamente? ")
#A função com validação para que o usuário compre
def compra_moedas():
    continuar = input("Gostaria de realizar Doações (Requer compra de creditos dentro do app)? ")
    if continuar == "sim" or continuar == "s":
        qtd = float(input("Informe a Quantidade de moedas que deseja comprar: "))
        #Validação Quantidade de moedas:
        if qtd < 10:
            while qtd < 10:
                qtd = float(input("A Quantidade de moedas deve se acima de 10 digite novamente (caso queira cancelar a compra digite 0):  "))   
                if qtd == 0:
                    exit(print("ok, Programa finalizado, volte sempre!"))
    else: exit(print("ok, Programa finalizado, volte sempre!"))
    return qtd 

#Função onde o usuário Realiza o pagamento 
def pagamento(qtd):
    pag = int(input('''
*_*===================================Qual a forma de pagamento?=============================*_*
        Digite (1) para Pix
        Digite (2) para Cartão
*_*==========================================================================================*_*
'''))
    match pag:
        case 1:
            dados_pag = []
            tipo = print("TIPO DE CHAVE: CNPJ")
            dados_pag.append(tipo)
            chave = print("NÙMERO DA CHAVE: 18356363000108")
            print("VALOR A SER PAGO: ", qtd)
            dados_pag.append(chave)
            confirma = input("Digite (sim) para realizar o pagamento: ")
            dados_pag.append(confirma)
            print("---------------------PAGAMENTO CONCLUIDO!!!----------------")
            return dados_pag
        case 2:
            dados_pag = []
            nr_cartão = float(input("Informe o número do cartão: "))
            dados_pag.append(nr_cartão)
            cd_seguraça = float(input("Informe o codigode segurança: "))
            dados_pag.append(cd_seguraça)
            tipo_cartão = input("Informe se o cartão é de débito ou Crédito: ")
            dados_pag.append(tipo_cartão)
            print("---------------------PAGAMENTO CONCLUIDO!!!----------------")
            return dados_pag
#A função exibira uma menu onde o usuário escolherá o cormercio que deseja comprar o alimento, a Ong 
def doacao():
    opcao = "sim"
    while opcao == "sim" or opcao == "s":
        dados_doacao = []
        comercios = int(input('''Informe o comercio qual deseja comparar os alimentos
        (1) Dia
        (2) Frigoyama
        (3) Assai
        (4) Carrefur 
        '''))
        dados_doacao.append(comercios)
        ong = int(input('''
*_*================================Informe a Ong que deseja doar==========================*_*
        (1) Caça-Fome
        (2) Banco de Alimentos
        (3) Hamburgada do Bem
        (4) Amigos do Bem
*_*=======================================================================================*_*
'''))
        alimento = input("Informe nome do alimento: ")
        dados_doacao.append(alimento)
        quantidade = int(input("Informe a quantidade: "))
        dados_doacao.append(quantidade)
        opcao = input("Deseja doar mais alimento? ")
    return dados_doacao
#Função para exibir o Extrato de pagamento
def extrato_doacao(pessoa, pagamento, alimento):
    print("\n===================Extrato de doação================================")
    print("Nome:" , pessoa[0])
    print("Documento: ", pessoa[1])
    print("Alimento:", alimento[1])
    print("Quantidades: ", alimento[0])
    print("\n====================================================================")
    print("Programa finalizado, volte sempre!")
#========================Programa Principal==============================#
escolha = menu_cadastro()
pessoa = cadastro(escolha)
menu_info()
qtd = compra_moedas()
dados_pag = pagamento(qtd)
dados_doacao = doacao()
extrato_doacao(pessoa, dados_pag, dados_doacao)
import os
import mysql.connector

database = False

class Produto:
    def __init__(self, codigo, nome, desc, custoProduto, custoAdministrativo, comissaoVendas, impostos, rentabilidade):
        self.codigo = codigo
        self.nome = nome
        self.desc = desc
        self.custoProduto = custoProduto
        self.custoAdministrativo = custoAdministrativo
        self.comissaoVendas = comissaoVendas
        self.impostos = impostos
        self.rentabilidade = rentabilidade
        self.precoVenda = custoProduto/(1-((custoAdministrativo + comissaoVendas + impostos + rentabilidade)/100))
        self.receitaBruta = self.precoVenda - custoProduto
        self.outrosCustos = custoAdministrativo + comissaoVendas + impostos

        if rentabilidade > 20:
            self.classificacaoRentabilidade = "Alta"
        if rentabilidade > 10 and rentabilidade <= 20:
            self.classificacaoRentabilidade = "Lucro médio"
        if rentabilidade > 0 and rentabilidade <= 10:
            self.classificacaoRentabilidade = "Lucro baixo"
        if rentabilidade == 0:
            self.classificacaoRentabilidade = "Equilibrio"
        if rentabilidade < 0:
            self.classificacaoRentabilidade = "Prejuizo"
    

def createTableOfProdutos(produto, sizeFirstcell, sizeMiddlecell, sizeLastcell):
    table = [
    ['Descricao', 'Valor', '%'],
    ['Preço de venda', round(produto.precoVenda, 2), '100%'], 
    ['Custo de aquisição', round(produto.custoProduto, 2), str(round(100 * (produto.custoProduto / produto.precoVenda), 2))+ "%" ], 
    ['Receita bruta', round(produto.receitaBruta, 2), str(round(100 * (produto.receitaBruta / produto.precoVenda), 2))+ "%"], 
    ['Custo fixo/administrativo', round(produto.custoAdministrativo, 2), str(round(100 * (produto.custoAdministrativo / produto.precoVenda), 2))+ "%"],
    ['Comissão de vendas', round(produto.comissaoVendas, 2), str(round(100 * (produto.comissaoVendas / produto.precoVenda), 2))+ "%"],
    ['Imposto', round(produto.impostos, 2), str(round(100 * (produto.impostos / produto.precoVenda), 2))+ "%"],
    ['Outros custos', round(produto.outrosCustos, 2), str(round(100 * (produto.outrosCustos / produto.precoVenda), 2))+ "%"],
    ['Rentabilidade', round(produto.receitaBruta - produto.outrosCustos,2), str(round(100 * ((produto.receitaBruta - produto.outrosCustos) / produto.precoVenda), 2))+ "%"],
    ['Classificação de lucro', produto.classificacaoRentabilidade, '']]
    for item in table:
                print("|",item[0]," "*(sizeFirstcell-len(str(item[0]))),"|",item[1]," "*(sizeMiddlecell-len(str(item[1]))),"|", item[2]," "*(sizeLastcell-len(str(item[2]))),"|")

def createProduto():
    utilizandoCriacaoDeProduto = True
    os.system("cls")
    while utilizandoCriacaoDeProduto:
        try:
            codigo = input("Digite o codigo do produto: ")
            nome = input("Digite o nome do produto: ")
            desc = input("Digite a descrição do produto: ")
            custoProduto = float(input("Digite o custo do produto: "))
            custoAdministrativo = float(input("Digite o custo fixo/administrativo do produto: "))
            comissaoVendas = float(input("Digite a comissão de venda do produto: "))
            impostos = float(input("Digite o valor dos impostos sobre o produto: "))
            rentabilidade = float(input("Digite a rentabilidade do produto: "))

            produto = Produto(codigo, nome, desc, custoProduto, custoAdministrativo, comissaoVendas, impostos, rentabilidade)

            os.system("cls")
            
            createTableOfProdutos(produto, 25, 25, 10)

            continuar = input("\n\n1-continuar\nOutros-Voltar ao menu\n\nDigite a sua escolha: ")
            utilizandoCriacaoDeProduto = continuar == "1"

        except ValueError:
            os.system("cls")
            print("O valor deve ser um número")
            tentarNovamente = input("1-Tentar novamente\nOutros-Voltar ao menu\n\nDigite a sua escolha: ")
            utilizandoCriacaoDeProduto = tentarNovamente == "1"

        except:
            print("Algo deu errado...")
            continuar = input("1-continuar\nOutros-Voltar ao menu\n\nDigite a sua escolha: ")
            utilizandoCriacaoDeProduto = continuar == "1"
    
    

def listProdutos():
    while True:
        os.system("cls")
        databaseConnection.reset_session()
        database.execute("select * from produtos;")
        list = database.fetchall()
        for item in list:
            produto = Produto(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
            print(str(produto.codigo) + " - " + produto.nome + " - " + produto.desc)
            print(createTableOfProdutos(produto, 25, 25, 10))
            print('\n\n\n')
        
        input("clique em qualquer tecla para voltar ao menu: ")
        break

def menu():
    utilizandoMenu = True
    while utilizandoMenu:
        os.system("cls")
        print("Bem-vindo ao projeto de cadastro de produto!!!")
        opcao = input(("1-Cadastrar produto\n2-Alterar produto\n3-Listar produto\n4-Deletar produto\nOutros-Sair do sistema\n\nDigite a opção escolhida: "))
        if opcao == "1":
            createProduto()
        if opcao == "2":
            print("função alterar")
        if opcao == "3":
            listProdutos()
        if opcao == "4":
            print("função deletar")
        if opcao not in ["1", "2", "3", "4"]:
            utilizandoMenu = False
            print("Até Logo!")


databaseConnection = mysql.connector.connect(host="127.0.0.1", database="projetoIntegrado", user="root", password="root")

if databaseConnection.is_connected():
    database = databaseConnection.cursor()
    menu()
else:
    print("Não foi possivel conectar ao banco de dados\ntente novamente mais tarde...")
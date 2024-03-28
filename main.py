import os

class Produto:
    def __init__(self, codigo, nome, desc, custoProduto, custoAdministrativo, comissaoVendas, impostos, rentabilidade, lucroDesejadoPorProduto):
        self.codigo = codigo
        self.nome = nome
        self.desc = desc
        self.custoProduto = custoProduto
        self.custoAdministrativo = custoAdministrativo
        self.comissaoVendas = comissaoVendas
        self.impostos = impostos
        self.rentabilidade = rentabilidade
        self.lucroDesejadoPorProduto = lucroDesejadoPorProduto
        self.magemLucro = (lucroDesejadoPorProduto/rentabilidade) * 100
        self.precoVenda = custoProduto/1-((custoAdministrativo + comissaoVendas + impostos + (lucroDesejadoPorProduto/rentabilidade) * 100)/100)
    

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
            lucroDesejadoPorProduto = float(input("Digite o lucro desejado por unidade: "))

            produto = Produto(codigo, nome, desc, custoProduto, custoAdministrativo, comissaoVendas, impostos, rentabilidade, lucroDesejadoPorProduto)

            os.system("cls")

            print("Codigo: " + produto.codigo + "\nNome: " + produto.nome + "\nDescrição: " + produto.desc + "\nCusto: " + str(produto.custoProduto) + "\nCusto fixo/administrativo: " + str(produto.custoAdministrativo) + "\nComissão de vendas: " + str(produto.comissaoVendas) + "\nImpostos: " + str(produto.impostos) + "\nRentabilidade: " + str(produto.rentabilidade) + "\nMargem lucro: " + str(produto.magemLucro) + "\nPreço de venda: " + str(produto.precoVenda) + "\n\n")

            continuar = input("1-continuar\nOutros-Voltar ao menu\n\nDigite a sua escolha: ")
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
            print("função listar")
        if opcao == "4":
            print("função deletar")
        if opcao not in ["1", "2", "3", "4"]:
            utilizandoMenu = False
            print("Até Logo!")


menu()

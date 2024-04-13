import os

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

            
            print("Descrição            |" + " valor  |" + " %")
            print("Preço de venda  | " + str(produto.precoVenda) + " | 100%")
            print("Custo do produto    | " + str(produto.custoProduto) + " | " + str(100 * (produto.custoProduto / produto.precoVenda)) + "%")
            print("Receita Bruta  | " + str(produto.receitaBruta) + " | " + str(100 * (produto.receitaBruta / produto.precoVenda))+ "%")
            print("Custo Administrativo/Fixo    | " + str(produto.custoAdministrativo) + " | " + str(100 * (produto.custoAdministrativo / produto.precoVenda))+ "%")
            print("Comissão de vendas    | " + str(produto.comissaoVendas) + " | " + str(100 * (produto.comissaoVendas / produto.precoVenda))+ "%")
            print("Impostos     | " + str(produto.impostos) + " | " + str(100 * (produto.impostos / produto.precoVenda))+ "%")
            print("Outros custos   | " + str(produto.outrosCustos) + " | " + str(100 * (produto.outrosCustos / produto.precoVenda))+ "%")
            print("Rentabilidade     | " + str(produto.receitaBruta - produto.outrosCustos) + " | " + str(100 * ((produto.receitaBruta - produto.outrosCustos) / produto.precoVenda))+ "%")
            print("Classificação de lucro  | " + str(produto.classificacaoRentabilidade))

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

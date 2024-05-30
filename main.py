import os

#-Dicionários-------------------------------------------------------------------
itens = {
  "0001" : ["Feijão", "Alimento", "Carioca"]
}
compras = {}
retiradas = {}
estoque = {}

#-FUNÇÕES-----------------------------------------------------------------------
def menu_despensa():
  os.system("clear")
  print()
  print("+----------------------+")
  print("|         MENU         |")
  print("|       DESPENSA       |")
  print("+----------------------+")
  print("| 1 - Itens            |")
  print("| 2 - Compras          |")
  print("| 3 - Retiradas        |")
  print("| 4 - Estoque          |")
  print("| 5 - Lista de Compras |")
  print("| 6 - Relatórios       |")
  print("| 7 - Informações      |")
  print("| 0 - Sair             |")
  print("+----------------------+")
  op_menu = input("| Escolha sua opção:")
  return op_menu


def menu_itens():
    os.system('clear')
    print()
    print("+----------------------+")
    print("|      MENU ITENS      |")
    print("+----------------------+")
    print("| 1 - Cadastrar        |")
    print("| 2 - Exibir Dados     |")
    print("| 3 - Remover Dados    |")
    print("| 0 - Voltar           |")
    print("+----------------------+")
    op_itens = input("| Escolha sua opção:")
    return op_itens

def cadastrar_itens():
  while True:
    os.system("clear")
    print("+-----------------------+")
    print("|    CADASTRAR ITENS    |")
    print("+-----------------------+")
    print("|")
    print("| <ENTER> para voltar")
    print("|")
    cod = input("| Código de 4 dígitos (XXXX):")
    print("|")
    if cod.strip() == '':
      break
    elif len(cod) == 4 and cod.isdigit():
      if cod not in itens:
        nome = input("| Nome:") #não permitir que o usuário coloque apenas espaço
        print("|")
        categoria = input("| Categoria:")
        print("|")
        marca = input("| Marca:")
        print("|")
        itens[cod] = [nome, categoria, marca]
        print("| Item cadastrado com sucesso!")
        print()
        input("<ENTER> para continuar")
      else:
        print("| Este código já foi cadastrado anteriormente!")
        print()
        input("<ENTER> para continuar")
#FINALIZAR ESSSA ÁREA###########################################################

op_menu = ""
while op_menu != "0":
  op_menu = menu_despensa()

  if op_menu == "1":
    op_itens = ""
    while op_itens != "0":
      op_itens = menu_itens()
      if op_itens == "1":
        cadastrar_itens()


      elif op_itens == "2":
        while True:
          os.system("clear")
          print("+----------------------+")
          print("|     EXIBIR DADOS     |")
          print("+----------------------+")
          print("|")
          print("| <ENTER> para voltar")
          print("|")
          cod = input("| Código de 4 dígitos (XXXX):")
          print("|")
          if cod.strip() == '':
            break
          elif len(cod) == 4 and cod.isdigit():
            if cod in itens:
              print("| Codigo:", cod)
              print("| Nome:", itens[cod][0])
              print("| Categoria:", itens[cod][1])
              print("| Marca:", itens[cod][2])
              print()
              input("<ENTER> para continuar")
            else:
              print("| Código inexistente!")
              print()
              input("<ENTER> para continuar")
      
      elif op_itens == "3":
        while True:
          os.system("clear")
          print("+-----------------------+")
          print("|     REMOVER DADOS     |")
          print("+-----------------------+")
          print("|")
          print("| <ENTER> para voltar")
          print("|")
          cod = input("| Código de 4 dígitos (XXXX):")
          print("|")
          if cod.strip() == '':
            break
          if len(cod) == 4 and cod.isdigit():
            if cod in itens:
              print("| Codigo:", cod)
              print("| Nome:", itens[cod][0])
              print("| Categoria:", itens[cod][1])
              print("| Marca:", itens[cod][2])
              print("|")
              resp = input("| Deseja REMOVER os dados do item acima (S/N)?")
              print("|")
              if resp.upper() == "S":
                del itens[cod] # MUDAR para tornar o item "False" em vez de deletar
                print("| Item Removido com Sucesso!")
                print()
                input("<ENTER> para voltar")
            else:
              print("| Código inexistente!")
              print()
              input("<ENTER> para voltar")

  elif op_menu == "2":
    os.system("clear")
    print("+----------------------+")
    print("|        COMPRA        |")
    print("+----------------------+")
    print("|")
    cod = input("| Insira o Código do produto:")
    print("|")
    if cod in itens:
      dt_hr = input("| Data e Hora da Compra:")
      print("|")
      valor = float(input("| Valor da unidade:"))
      print("|")
      quantidade = int(input("| Quantidade comprada:"))
      compras[dt_hr] = [cod, valor, quantidade]
      estoque[cod] = [quantidade] # Pro estoque vou adicionar um verificador de quantidade, para que ele adicione em vez de alterar
      print(compras)
      print("| Compra cadastrada com sucesso!")
    else:
      print("| O código não corresponde a nenhum item da despensa!")
      #resp = input ("Deseja cadastrar um item na despensa (S/N)?")
    print()
    input("<ENTER> para voltar")

  elif op_menu == "3":
    os.system("clear")
    print("+----------------------+")
    print("|       RETIRADA       |")
    print("+----------------------+")
    print("|")
    cod = input("| Insira o Código do produto:")
    print("|")
    if cod in itens:
      dt_hr = input("| Data e Hora da Retirada:")
      print("|")
      quant_ret = int(input("| Quantidade Retirada:"))
      quantidade = estoque[cod][0] - quant_ret #para a quantidade salva no dicionário ser a quantidade que restou
      retiradas[dt_hr] = [cod, quantidade]
      estoque[cod] = quantidade
      print(retiradas)
      print("| Retirada cadastrada com sucesso!")
    else:
      print("| O código não corresponde a nenhum item da despensa!")
    print()
    input("<ENTER> para voltar")


  elif op_menu == "4":
    os.system('clear')
    op_est = ""
    print()
    print("+-------------------+")
    print("|      ESTOQUE      |")
    print("+-------------------+")
    print("|")
    print(estoque)
    print()
    input("| <ENTER> para voltar")

################################################################################

  elif op_menu == "5":
    os.system('clear')
    op_list = ""
    print()
    print("+----------------------------+")
    print("|      LISTA DE COMPRAS      |")
    print("+----------------------------+")
    print("|")
    # Variável que recebe os itens que atingiram o estoque minimo
    print()
    input("| <ENTER> para voltar")


  elif op_menu == "6":
    os.system("Clear")
    op_rel = ""
    while op_rel != "0":
      os.system('clear')
      print()
      print("+-------------------------------+")
      print("|      RELATÓRIOS DE ITENS      |")
      print("+-------------------------------+")
      print("| 1 - Itens Faltando            |")
      print("| 2 - Itens em Baixa Quantidade |")
      print("| 3 - Itens em Alta Quantidade  |")
      print("| 4 - Itens Baratos             |")
      print("| 5 - Itens Caros               |")
      print("| 5 - Itens por Categoria       |")
      print("| 5 - Itens Marca               |")
      print("| 0 - Voltar                    |")
      print("+-------------------------------+")
      input("| Escolha sua opção:")

  elif op_menu == "7":
    os.system('clear')
    op_inf = ""
    print()
    print("+---------------------------------------------+")
    print("|                 INFORMAÇÕES                 |")
    print("+---------------------------------------------+")
    print("| Projeto de Controle de Despensa             |")
    print("| Desenvolvedor: Guilherme Araújo / oguiaraujo|")
    print("+---------------------------------------------+")
    input("| <ENTER> para voltar")

print("Programa Encerrado!")
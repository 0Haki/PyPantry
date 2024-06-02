import os
import re

#-Dicionários-------------------------------------------------------------------
itens = {}
compras = {}
retiradas = {}
estoque = {}

#-FUNÇÕES-----------------------------------------------------------------------
def validar_data_hora(data_hora):
  regex = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4} (0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$'
  if re.match(regex, data_hora):
      return True
  else:
      return False


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


def exibir_dados():
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


def remover_dados():
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
          input("<ENTER> para contuniar")
      else:
        print("| Código inexistente!")
        print()
        input("<ENTER> para continuar")

#-PROGRAMA PRINCIPAL------------------------------------------------------------
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
        exibir_dados()      
      elif op_itens == "3":
        remover_dados()
        
  elif op_menu == "2":
    while True:
      os.system("clear")
      print("+----------------------+")
      print("|        COMPRA        |")
      print("+----------------------+")
      print("|")
      print("| <ENTER> para voltar")
      print("|")
      cod = input("| Código existente de 4 dígitos (XXXX):")
      print("|")
      if cod.strip() == '':
        break
      if len(cod) == 4 and cod.isdigit():
        if cod in itens:
          data_hora = input("| Data e Hora da COMPRA (DD/MM/AAAA HH:MM):")
          if validar_data_hora(data_hora):
            while True:
                insira_valor = re.compile("^R\$ \d+(\.\d{1,2})?$")
                valor = input("| Valor da unidade (R$ XX.XX):")
                if insira_valor.match(valor):
                  break
                else:
                  ValueError
            while True:
              try:
                quantidade = int(input("| Quantidade a ser adicionada:"))
                break
              except ValueError:
                print()
                print("| Insira uma quantidade válida")
                print()
            compras[data_hora] = [cod, valor, quantidade]
            if cod in estoque:
              estoque[cod] += quantidade
            else:
              estoque[cod] = quantidade
            if data_hora in compras:
              print("|")
              print("| Código:", compras[data_hora][0])
              print("| Valor da unidade:", compras[data_hora][1])
              print("| Quantidade comprada:", compras[data_hora][2])
              print("|")
              print("| Compra cadastrada com sucesso!")
              print()
              input("<ENTER> para continuar")
          else:
            print("Insira uma data e hora válida")
            print()
            input("<ENTER> para continuar")
        else:
          print("| O código inexistente!")
          print()
          input("<ENTER> para continuar")


  elif op_menu == "3":
    while True:
      os.system("clear")
      print("+----------------------+")
      print("|       RETIRADA       |")
      print("+----------------------+")
      print("|")
      print("| <ENTER> para voltar")
      print("|")
      cod = input("| Código existente de 4 dígitos (XXXX):")
      print("|")
      if cod.strip() == '':
        break
      if len(cod) == 4 and cod.isdigit():
        if cod in itens:
          data_hora = input("| Data e Hora da RETIRADA (DD/MM/AAAA HH:MM):")
          if validar_data_hora(data_hora):
            while True:
              try:
                quantidade = int(input("| Quantidade a ser retirada:"))
                break
              except ValueError:
                print()
                print("| Insira uma quantidade válida")
                print()
            retiradas[data_hora] = [cod, quantidade]
            if cod in estoque:
                  if estoque[cod] >= quantidade:
                    estoque[cod] -= quantidade
                    if estoque[cod] == 0:
                      del estoque[cod]
                  else:
                    print("| Quantidade insuficiente no estoque")
                    print()
            if data_hora in retiradas:
              print("|")
              print("| Código:", retiradas[data_hora][0])
              print("| Quantidade retirada:", retiradas[data_hora][1])
              print("|")
            print("| Retirada cadastrada com sucesso!")
            print()
            input("<ENTER> para continuar")
          else:
            print("| Código inexistente!")
            print()
            input("<ENTER> para continuar")


  elif op_menu == "4":
    os.system('clear')
    op_est = ""
    print()
    print("+-------------------+")
    print("|      ESTOQUE      |")
    print("+-------------------+")
    print("|")
    for cod, quantidade in estoque.items():
      print("| ", cod, "|", quantidade)
    print()
    input("| <ENTER> para voltar")


  elif op_menu == "5":
    os.system('clear')
    op_list = ""
    print()
    print("+----------------------------+")
    print("|      LISTA DE COMPRAS      |")
    print("+----------------------------+")
    print("|")
    for cod, quantidade in estoque.items():
      if quantidade <= 5:
        print("| ",cod,"|", itens[cod][0])
    print()
    input("| <ENTER> para voltar")


  elif op_menu == "6":
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
      print("| 4 - Itens por Valor           |")
      print("| 5 - Itens por Categoria       |")
      print("| 6 - Itens por Marca           |")
      print("| 0 - Voltar                    |")
      print("+-------------------------------+")
      op_rel = input("| Escolha sua opção:")

      if op_rel == "1":
        os.system("clear")
        print("+--------------------------------+")
        print("|         ITENS FALTANDO         |")
        print("+--------------------------------+")
        print("|")
        for cod, quantidade in estoque.items():
          if quantidade == 0:
            print("| ",cod,"|", itens[cod][0])
        print()
        input("| <ENTER> para voltar")
      
      elif op_rel == "2":
        os.system("clear")
        print("+--------------------------------+")
        print("|        BAIXA QUANTIDADE        |")
        print("+--------------------------------+")
        print("|")
        for cod, quantidade in estoque.items():
          if quantidade <= 5:
            print("| ",cod,"|", itens[cod][0])
        print()
        input("| <ENTER> para voltar")

      elif op_rel == "3":
        os.system("clear")
        print("+---------------------------------+")
        print("|         ALTA QUANTIDADE         |")
        print("+---------------------------------+")
        print("|")
        for cod, quantidade in estoque.items():
          if quantidade >= 50:
            print("| ",cod,"|", itens[cod][0])
        print()
        input("| <ENTER> para voltar")

      elif op_rel == "4":
        os.system("clear")
        print("+---------------------------------+")
        print("|         ITENS POR VALOR         |")
        print("+---------------------------------+")
        print("|")
        while True:
          insira_valor = re.compile("^R\$ \d+(\.\d{1,2})?$")
          valor_procurado = input("| Valor da unidade (R$ XX.XX):")
          if insira_valor.match(valor_procurado):
            break
          else:
            ValueError
        for data_hora, valor in compras.items():
          if valor_procurado in compras[data_hora]:
            apenas_data = 10
            print("| Na data",data_hora[:apenas_data], "o item:", compras[data_hora][0],"Custava", valor_procurado)
        print()
        input("| <ENTER> para voltar")

      elif op_rel == "5":
        os.system("clear")
        print("+---------------------------------+")
        print("|       ITENS POR CATEGORIA       |")
        print("+---------------------------------+")
        print("|")
        categoria_procurada = input("| Categoria:")
        print("|")
        for cod, categoria in itens.items():
          if categoria_procurada in itens[cod]:
            print("| ", cod, "|", itens[cod][0])
        print()
        input("| <ENTER> para voltar")

      elif op_rel == "6":
        os.system("clear")
        print("+---------------------------------+")
        print("|         ITENS POR MARCA         |")
        print("+---------------------------------+")
        print("|")
        marca_procurada = input("| Marca:")
        print("|")
        for cod, marca in itens.items():
          if marca_procurada in itens[cod]:
            print("| ", cod, "|", itens[cod][0])
        print()
        input("| <ENTER> para voltar")


  elif op_menu == "7":
    os.system('clear')
    print()
    print("+---------------------------------------+")
    print("|                 INFORMAÇÕES           |")
    print("+---------------------------------------+")
    print("| Projeto de Controle de Despensa       |")
    print("| Desenvolvedor: Guilherme Araújo       |")
    print("| GitHub: oguiaraujo                    |")
    print("| replit: oguiaraujo                    |")
    print("| instagram: somuliro                   |")
    print("+---------------------------------------+")
    print()
    input("| <ENTER> para voltar")

print("Programa Encerrado!")
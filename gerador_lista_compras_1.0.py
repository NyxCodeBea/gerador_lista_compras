# --- 1. Configurações e Dados ---

import sys

ingredientes_lista = []
quantidades_ingredientes = []
lista_vizualizacao = []


def vizualizacao_lista(add_ingredientes, add_quantidade):
    print(f"Foi solicitado o ingrediente {add_ingredientes} com {add_quantidade} unidades.")


try:
    with open("lista_compras.txt", "r") as arquivo:
        for linha in arquivo.readlines():
            # Passo A: Limpar e Cortar
            pedacos = linha.strip().split(" - ")

            # Passo B: O FILTRO DE SEGURANÇA
            if len(pedacos) == 2:
                # --- A CORREÇÃO É AQUI ---
                # Removemos o texto " unidades." para guardar apenas o número na memória
                pedacos[1] = pedacos[1].replace(" unidades.", "") 
                
                lista_vizualizacao.append(pedacos)

except FileNotFoundError:
    print("Ainda não existe uma lista salva. Começando uma nova!")

print("Bem-Vindo Chef, ao sistema de solicitação Lista de Compras. \n")

# --- 1. Menu Inicial ---

while True:
    verificacao = input("Você quer ir para Ingredientes (I), Arquivos (A) ou Fechar (F)? ")

    if(verificacao.upper() == "F"):
        print("Fechando o programa lista de compras!")
        break

    elif(verificacao.upper() == "I"):
        # --- 3. Criação da Lista de Compras ---
        while True:
            solicitacao = input("Deseja acrescentar ingredientes a lista de compras? Abrir (O) / Adicionar (A) / Sair (S) / Visualizar (V): ")
            if(solicitacao.upper() == "S"):
                print("Fim da solicitação da lista de compras!")
                break
            
            elif(solicitacao.upper() == "A"):
                try:
                    add_ingredientes = input("Digite o nome do ingrediente: ").title()
                    add_quantidade = int(input("Digite a quantidade de ingrediente: "))

                    ticket = [add_ingredientes, add_quantidade]
                    lista_vizualizacao.append(ticket)
                    print(f"Ingrediente {add_ingredientes} foi adicionado com sucesso a sua lista de compras!")

                except ValueError:
                    print("Ops! Você precisa digitar um número válido.")

            elif(solicitacao.upper() == "O"):
                abrir = open("lista_compras.txt", "r")

                for linhas in abrir.readlines():  
                    print(linhas.strip())
                abrir.close()
            else:
                # --- 4. Visualizando a Lista ---
                print("--- VISUALIAÇÃO DA LISTA --- \n")
                for ticket in lista_vizualizacao:
                    vizualizacao_lista(ticket[0], ticket[1])

    elif(verificacao.upper() == "A"):
        # --- 5. Arquivo ---
        while True:
            print("O que deseja fazer?")
            verificacao = input(" Escrever um novo arquivo (C) / Adicionar mais uma linha (A) / Remover (R) / Sair (S): ")

            if(verificacao.upper() == "S"):
                print("Saindo....")
                break

            elif(verificacao.upper() == "C"):
                try:
                    # 1. Limpa a memória (Começar do zero)
                    lista_vizualizacao = [] 

                    # 2. Abre o arquivo e apaga tudo o que tinha lá (Modo 'w')
                    with open("lista_compras.txt", "w") as arquivo:
                        arquivo.write("--- LISTA DE COMPRA --- \n")
                        # Como a lista está vazia, o loop for não vai escrever nenhum ingrediente.
                        # O arquivo final terá apenas o título.

                    print("Sucesso! A lista foi reiniciada do zero.")

                except ValueError:
                    print("Ops! Você precisa digitar uma opção válida.")

            elif(verificacao.upper() == "A"):
                try:
                    with open("lista_compras.txt", "w") as arquivo:
                        arquivo.write("--- LISTA DE COMPRA --- \n")
                        for lista in lista_vizualizacao:
                            arquivo.write(f"{lista[0]} - {lista[1]} unidades. \n")

                    print("Sucesso! Mais um item foi adicionado em sua lista.")

                except ValueError:
                    print("Ops! Você precisa digitar uma opção válida.")
            
            elif(verificacao.upper() == "R"):
                try:
                    ab = open("lista_compras.txt", "r")
                    linhas = ab.readlines()
                    ab.close()

                    for i, linha in enumerate(linhas):
                        print(f"{i}: {linha.strip()}")
                    
                    remover = int(input("Qual intem da lista deseja remover? "))

                    while(remover == 0):
                        print("Ops, opção inválida!")
                        remover = int(input("Qual intem da lista deseja remover? "))

                    linhas.pop(remover)

                    with open("lista_compras.txt", "w") as arquivo:
                        for linha in linhas:
                            arquivo.write(linha)
                except FileNotFoundError:
                    print("Ainda não existe uma lista para remover itens!")
                
            else:
                    print("Ops! Você precisa digitar uma opção válida.")
    else:
        print("Ops, houve um erro de digitação....")





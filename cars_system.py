from pickle import *
import os

def menu():
    os.system('cls')
    print("**********************")
    print("*   Menu Principal   *")
    print("**********************\n")
    print("  1 - Cadastrar carro")
    print("  2 - Vender carro")
    print("  3 - Listar ordenado pela marca")
    print("  4 - Listar ordenado pelo modelo")
    print("  5 - Listar ordenado pela preço")
    print("  0 - Sair \n")
    return input("  Escolha uma opção: ")

def inserirCarro(carros):
    cod = int(input("\n Código: "))
    r = venderCarro(cod, carros)
    if r >= 0:
        print("\n --- Carro já cadastrado --- \n")
    else:
        marc = input("\n Marca: ").upper()
        modl = input("\n Modelo: ").upper()
        ano = int(input("\n Ano: "))
        cor = input("\n Cor: ").upper()
        val = float(input("\n Preço: "))
        carros.append([cod, marc, modl, ano, cor, val])
        os.system("pause")

def mostrarCarros(carros):
    print("-------------------------------------------------------------")
    print(" COD MARCA           MODELO          ANO  COR        PREÇO   ")
    print(" --- --------------- --------------- ---- ---------- --------")
    for i in range(len(carros)):
        print(" {:03d} {:15s} {:15s} {:4d} {:10s} {:.2f}".format(carros[i][0], carros[i][1], carros[i][2], carros[i][3], carros[i][4], carros[i][5]))
    os.system("pause")
    

def venderCarro(cod, carros):
    for i in range(len(carros)):
        if int(cod) == carros[i][0]:
            return i
    return -1



def principal():
    save = False
    try:
        sf = open("carros.arq", "rb")
        carros = load(sf)
        sf.close()
    except FileNotFoundError:
        print("\n --- Nenhum carro cadastrado --- \n")
        carros = []
    op = '1'
    while op != '0':
        op = menu()
        if op == '1':
            print("\n  --- Novo Carro --- \n")
            inserirCarro(carros)
            save = True
        elif op == '2':
            print("\n  --- Vender Carro ---\n")
            cod = int(input("\n Código: "))
            r = venderCarro(cod, carros)
            if r < 0:
                print("\n --- Carro não cadastrado --- \n")
            else:
                a = "w"
                while a != "S" and a != "s" and a != "N" and a != "n":
                    print("\n Será removido do cadastro.")
                    a = input("Confirma?(s/n): ")
                    if a == "S" or a == "s":
                        del carros[r]
                        save = True
                        print("\n --- Carro removido ---")
        elif op == '3':
            print("\n Lista de carros pela marca: ")
            carros = sorted(carros, key = lambda x : x[1])
            mostrarCarros(carros)
            print("")
        elif op == '4':
            print("\n Lista de carros pel modelo: ")
            carros = sorted(carros, key = lambda x : x[2])
            mostrarCarros(carros)
            print("")
        elif op == '5':
            print("\n Lista de carros pel preço: ")
            carros = sorted(carros, key = lambda x : x[5])
            mostrarCarros(carros)
            print("")
        elif op == '0':
            if save:
                s = "a"
                while s != "S" and s != "s" and s != "N" and s != "n":
                    s = input("\n Deseja salvar as alterações feitas?(s/n): ")
                    if s == "S" or s == "s":
                        sf = open("carros.arq", "wb")
                        dump(carros, sf)
                        sf.close()
                        print("\n Alterções salvas com sucesso")
            print("\n --- Fim do Aplicativo --- \n")
        else:
            print("\n  *** Opção inválida ***\n")

principal()

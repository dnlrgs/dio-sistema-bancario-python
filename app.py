MENU_1 = """
[1] - SALDO
[2] - SACAR
[3] - DEPOSITAR
[4] - EXTRATO
"""
#MENU_2 = """
#[1] - SALDO
#[2] - SACAR
#[3] - DEPOSITAR
#[4] - EXTRATO
#
#[5] - MENU INICIAL
#"""

opcao_operação = 0 
saldo = 10
moeda = "R$"

while True:

    opcao_operação = input(MENU_1)
    
    if opcao_operação == "2":
        valor_saque = int(input(f"""SALDO = {moeda}{saldo:.2f}.
              INFORMAR VALOR A SER SACADO:
              """))
        if valor_saque > saldo:
            print(f"Saldo ({moeda}{saldo:.2f}) insuficiente.")
        else:
            saldo -=valor_saque
            print(f"O seu saque está sendo processado. Por favor, retire o valor do caixa.")
    elif opcao_operação == "3":
        valor_depositado = int(input("Favor insirir o valor a ser depositado."))
        saldo += valor_depositado
        print(f"Seu novo saldo é {moeda}{saldo}.")
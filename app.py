MENU_1 = """
[1] - SALDO
[2] - SACAR
[3] - DEPOSITAR
[4] - EXTRATO
"""

opcao_operação = 0 
saldo = 10
moeda = "R$"
VALOR_LIMITE_POR_SAQUE = 500
qtd_saques_dia = 0
QTD_LIMITE_SAQUES_DIA = 3
extrato_vazio = """
EXTRATO

"""

extrato = """
EXTRATO

"""

while True:

    opcao_operação = input(MENU_1)
    
    if opcao_operação == "2":
        if saldo == 0 or qtd_saques_dia == QTD_LIMITE_SAQUES_DIA:
            if saldo == 0:
                print(f"Não é possível realizar saques, seu saldo é de {moeda}0.00.")
            else:
                print(f"""O limite de {QTD_LIMITE_SAQUES_DIA} saques do dia já foi atingido.""")        

        
        else:
            valor_saque = float(input(f"""SALDO = {moeda}{saldo:.2f}.
              INFORMAR VALOR A SER SACADO:
              """))
            if valor_saque > saldo or valor_saque > VALOR_LIMITE_POR_SAQUE:
                if valor_saque > saldo:
                    print(f"Saldo ({moeda}{saldo:.2f}) insuficiente.")
                else:
                    print(f"Valor limite para saque é de {moeda}{VALOR_LIMITE_POR_SAQUE}.")
            else:
                saldo -=valor_saque
                qtd_saques_dia += 1
                print(f"O seu saque está sendo processado. Por favor, retire o valor do caixa.")
                extrato += f"""
                - SAQUE NO VALOR DE {moeda}{valor_saque}.
                SALDO: {saldo}"""

    elif opcao_operação == "3":
        valor_depositado = float(input("Favor insirir o valor a ser depositado."))
        saldo += valor_depositado
        print(f"Seu novo saldo é {moeda}{saldo}.")
        extrato += f"""
        - DEPOSITO NO VALOR DE {moeda}{valor_depositado}.
        SALDO: {saldo}"""
    elif opcao_operação == "1":
        print(f"{moeda}{saldo}")
    elif opcao_operação == "4":
        if extrato == extrato_vazio:
            print("Não há transações no momento.")
        else:
            print(f"""
            EXTRATO:
            {extrato}""")    
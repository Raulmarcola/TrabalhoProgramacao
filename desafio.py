
# DADOS
cargos = []
funcionarios = []

# FUNÇÕES
def imprimir_menu():
    
    print("\nMENU")
    print("1. Cadastrar os cargos da empresa.")
    print("2. Cadastrar os funcionários da empresa.")
    print("3. Mostrar um relatório contendo o número, o nome e o valor do salário de todos os funcionários.")
    print("4. Mostrar o valor pago aos funcionários que pertençam a um cargo informado pelo usuário.")
    print("5. Finalizar.")



def opcao1():
    
    if len( cargos ) == 0:
        
        for i in range(5):
            c = float( input(f'\nInforme o salário do cargo {i+1}:  ') )
            cargos.append( c )

        print(f'\nCargos Cadastrados \n')
        for i in range(len(cargos)):
            print(f'Cargo {i+1}: R$ {cargos[i]}')

    else: print("\nSalários dos cargos já cadastrados.")


def opcao2():
    if len(cargos) > 0:
        if len(funcionarios) < 15:

            #Número do Funcionário
            print('\nSobre o funcionário, informe: ')
            numero = int(input('\nNúmero: '))
            while verificaCodigo(numero, funcionarios):
                numero = int(input("\nNúmero deve ser único por funcionário \nNúmero: "))

            #Nome
            nome = input('\nNome: ')
            while verificaNome(nome):
                nome = input('\nNome deve ser composto \nNome: ')

            #Código do Cargo
            codigoCargo = int(input('\nCódigo do cargo: '))
            while verificaCodCargo(codigoCargo):
                codigoCargo = int(input('\nCódigo deve estar entre 1 e 5 \nCódigo do Cargo: '))

            #Transformando em um dicionário
            funcionario = {
                'numero': numero,
                'nome': nome,
                'codigoCargo': codigoCargo
            }

            #Colocando na lista
            funcionarios.append(funcionario)

        else: 
            print(f'\nLimite de funcionários atingido')
    else:
        print('\nCargos Não cadastrados.')

def verificaCodigo(numero, funcionarios):
    existente = False
    for i in range (len(funcionarios)):
        if numero == funcionarios[i]['numero']:
            existente = True
            return existente
        else:
            existente = False
    return existente

def verificaNome(nome):
    if ' ' in nome and not nome.endswith(' '): #Se o nome tiver espaço e houver algo depois, ou seja, não terminar com espaço (not endswith(' ')) quer dizer que é composto 
        return False #Nome tem espaço, então passa
    else:
        return True #True irá fazer o while repetir

def verificaCodCargo(codigoCargo):
    if 1 <= codigoCargo <= 5:
        return False
    else: 
        return True

def opcao3():
    if len(funcionarios) > 0:
        print('\nRelatório de Funcionários - ')

        #for i in funcionarios: Desta maneira, i assume os valores da lista de funcionários
            #print(i)

        for i in range(len(funcionarios)):
            salario = cargos[funcionarios[i]['codigoCargo'] -1]

            print(f'\nFuncionário {i+1} - \nNúmero: {funcionarios[i]["numero"]}\nNome: {funcionarios[i]["nome"]} \nSalário: R$ {salario}')

    else:
        print('\nFuncionários não cadastrados.')


def opcao4():
    if len(funcionarios) > 0:
        contador = 0
        codigoCargo = int(input('\nInforme o código do Cargo: '))
        while verificaCodCargo(codigoCargo):
            codigoCargo = int(input('\nCódigo deve estar entre 1 e 5 \nCódigo do Cargo: '))
            
        for i in funcionarios: #Desta maneira, i assume os valores da lista de funcionários
            if codigoCargo == i['codigoCargo']:
                contador += 1

        somatorio = cargos[codigoCargo - 1] * contador

        print(f'\nSoma dos salários do cargo {codigoCargo}: {somatorio}')
    else:
        print(f'\nFuncionários não cadastrados.')


def opcao5():
    print("\nOBRIGADO!")


def opcao_invalida():
    print("\nOpção inválida! Informe um número inteiro entre 1 e 5.")


# INÍCIO DO PROGRAMA
print("\nINÍCIO DO PROGRAMA")


opcao = -1
while( opcao != 5 ):

    imprimir_menu()

    opcao = int( input("\nInforme a opção desejada: ") )

    if opcao == 1: opcao1()
    elif opcao == 2: opcao2()
    elif opcao == 3: opcao3()
    elif opcao == 4: opcao4()
    elif opcao == 5: opcao5()
    else: opcao_invalida()


# FIM DO PROGRAMA
print("\nFIM DO PROGRAMA")
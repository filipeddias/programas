from time import sleep
print('CADASTRO DE PESSOAS NA EMPRESA')
sair_entrada = False
senhas = list()
n = 0
pessoas = list()
while not sair_entrada:
    print('''[ 1 ] Cadastrar pessoa
[ 2 ] Saida da pessoa
[ 3 ] ENCERRAR PROGRAMA
''')
    opc_entrada = int(input('Digite um dos valores acima: '))
    if opc_entrada == 1:
        sair_cadastro = False
        num = 0
        while not sair_cadastro:
            name = str(input('Digite o nome da pessoa: '))
            idade = str(input('Idade da pessoa: '))
            sexo = str(input('Qual genêro dele(a): '))
            cpf = int(input('Digite o CPF da pessoa (somente os números): '))
            andar = str(input('Andar que a pessoa vai: '))
            sala = str(input('Qual sala: '))
            sair = False
            while not sair:
                r = int(input('''OPÇÕES:
[ 1 ] ADICIONAR SENHA
[ 2 ] SAIR'''))
                if r == 1:
                    n += 1
                    print(f'A senha da pessoa é {n}')
                    if n not in senhas:
                        senhas.append(n)
                    else:
                        n += 1
                        senhas.append(n)
                    sair= True
                elif r == 2:
                    print('Saindo...')
                    sair = True
            print('''Opções: 
[ 1 ] Revisar cadastro
[ 2 ] Realizar novo cadastro
[ 3 ] Encerrar Processo''')
            opc = int(input('Qual sua escolha: '))
            if opc == 1:
                print(f'{name}\n{idade}\n{sexo}\n{cpf}\n{andar}\n{sala}\nSenha da pessoa {n}')
                print('''[ 1 ] Realizar novo cadastro
[ 2 ] Encerrar Processo''')
                opc1 = int(input('Qual é a sua escolha: '))
                if opc1 == 2:
                    sair_cadastro = True
                    print('ENCERRANDO PROCESSO.....')
                    sleep(2)
            elif opc == 3:
                sair_cadastro = True
                print('ENCERRANDO PROCESSO.....')
                sleep(2)
    elif opc_entrada == 2:
        print(senhas)
        remove = int(input('Digite a senha que deseja remover: '))
        senhas.remove(remove)
    elif opc_entrada == 3:
        sair_entrada = True
    elif opc_entrada == 4:
        print(pessoas)
print('''************
* OBRIGADO *
************''')

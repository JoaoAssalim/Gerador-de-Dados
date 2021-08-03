#Importando Libs
import random
import time
#Dados Falsos
Nomes = ['José', 'João', 'Matheus', 'Rivelino', 'Bruno', 'Clara', 'Maria', 'Elenice', 'Carlos', 'Antonio','Andre','Clarice','Felipe']
Sobrenomes = ['Silva', 'Almeida', 'Costa', 'Souza', 'Andrade', 'Munhoz','Jesus','Mendonca','Lopes','Barros']
Email = ['xxx@gmail.com.br', 'Modrad@gmail.com', 'Souzinha@gmail.com', 'Theus12@gmail.com', 'jooj123@gmail.com', 'nice1@gmail.com']
#Armazenamento de dados
bd = []

while True:
    #armazenamento para cpf
    numero1 = []
    numero2 = []
    numero3 = []
    digito = []

    #gerador de numeros aleatorios
    numero1.append(random.randint(100, 999))
    numero2.append(random.randint(100, 999))
    numero3.append(random.randint(100, 999))
    digito.append(random.randint(10, 99))
    #tirando aspas e chaves das listas
    numero1 = str(numero1)[1:-1]
    numero2 = str(numero2)[1:-1]
    numero3 = str(numero3)[1:-1]
    digito = str(digito)[1:-1]
    #transformando e armazenando os numeros em cpf
    cpf = f'{numero1}.{numero2}.{numero3}-{digito}'

    #Gerando dados
    choice_Nomes = random.choice(Nomes)
    choice_Sobrenomes = random.choice(Sobrenomes)
    choice_Email = random.choice(Email)
    
    #Interface 
    print('-'*30)
    print('GERADOR DE FALSOS DADOS')
    print('-'*30)
    time.sleep(1)
    
    print('[1] Ver dados gerados')
    print('[2] Gerar Dados')
    print('[3] Sair do Programa')
    time.sleep(1)
    escolha = input('Qual opção deseja executar? ')
    time.sleep(1)
    
    if not escolha.isdigit():
        print('Digite um numero da proxima vez!')
        again = input('Deseja continuar usando o programa? [S/N]').upper()
        if not again.isdigit():
            if again == 'N':
                break
    elif escolha.isdigit():
        escolha = int(escolha)
        if escolha > 0 and escolha < 4:
            if escolha == 1:
                if len(bd) == 0:
                    print('Nenhum dado gerado!')
                elif len(bd) != 0:
                    print(f'CPF: {bd[0::4]}\nNome: {bd[1::4]}\nSobrenome: {bd[2::4]}\nEmail: {bd[3::4]}')
            elif escolha == 2:
                bd.append(cpf)
                print(f'CPF: {cpf}')
                bd.append(choice_Nomes)
                print(f'Nome: {choice_Nomes}')
                bd.append(choice_Sobrenomes)
                print(f'Sobrenome: {choice_Sobrenomes}')
                bd.append(choice_Email)
                print(f'Email: {choice_Email}')
            elif escolha == 3:
                print('Até mais!')
                time.sleep(1)
                break
        else:
            print('Numero não valido!')
            again = input('Deseja continuar usando o programa? [S/N]').upper()
            if not again.isdigit():
                if again == 'N':
                    break
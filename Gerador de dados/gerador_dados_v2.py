import random

print('-='*20)
print('Bem Vindo ao Gerador de Dados'.center(40))
print('-='*20)

dados = []
#Listas com dados
nomes = ['José', 'João', 'Matheus', 'Rivelino', 'Bruno', 'Clara', 'Maria', 'Elenice', 'Carlos', 'Antonio','Andre','Clarice','Felipe']
sobrenomes = ['Silva', 'Almeida', 'Costa', 'Souza', 'Andrade', 'Munhoz','Jesus','Mendonca','Lopes','Barros']
dominio_email = ['@gmail.com', '@yahoo.com.br', '@outlook.com','@oul.com.br']

while True:
    nome_gerado = random.choice(nomes)
    sobrenome_gerado = random.choice(sobrenomes)
    email_gerado = random.choice(dominio_email)
    email_final = nome_gerado + sobrenome_gerado + email_gerado
    #gerando cpf
    num1 = random.randint(100,999)
    num2 = random.randint(100,999)
    num3 = random.randint(100,999)
    dig = random.randint(10, 99)
    cpf = f'{num1}.{num2}.{num3}-{dig}'
    print()
    print('[1] Gerar Dados Novos\n[2] Mostrar Dados Gerados\n[3] Encerrar Programa\n')

    escolha = input('Qual opcao deseja? ')

    if not escolha.isdigit():
        print('Digite um numero da proxima vez! ;(')
        break
    elif escolha.isdigit():
        escolha = int(escolha)
        if escolha == 1:
            dados.append(cpf)
            print(f'CPF: {cpf}')
            dados.append(nome_gerado)
            print(f'Nome: {nome_gerado}')
            dados.append(sobrenome_gerado)
            print(f'Sobrenome: {sobrenome_gerado}')
            dados.append(email_final)
            print(f'Email: {email_final}')
        elif escolha == 2:
            if len(dados) == 0:
                print('Nenhum dado gerado!')
            elif len(dados) != 0:
                print(f"Nomes: {dados[1::4]}\nSobrenomes: {dados[2::4]}\nEmail's: {dados[3::4]}\nCPF's: {dados[0::4]}")
        elif escolha == 3:
            print('Tchau brigado')
            break
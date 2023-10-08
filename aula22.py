# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

while True:
    entrada = input('[E]ntrar [S]air: ')
    if entrada in ('E, e'):
        senha_digitada = input('Senha: ')
        senha_permitida = '123456'

        if (entrada == 'E' or entrada == 'e')\
           and senha_digitada == senha_permitida:
            print('Entrar')
            break
        elif senha_digitada != senha_permitida:
            print('Senha incorreta!')
        else:
            print('Sair')
            break
    elif entrada in ('S, s'):
        print('Sair')
        break
    else:
        print('Input não suportado.')

# Avaliação de curto circuito
# senha = input('Senha: ') or 'Sem senha'
# print(senha)

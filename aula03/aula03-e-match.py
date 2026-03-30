escolha_usuario = 12

match escolha_usuario:
    case 0:
        status = 'sair do programa'
    case 1:
        status = 'entrar no programa'
    case _:
        status = 'erro'

print(status)
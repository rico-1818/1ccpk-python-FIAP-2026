from model import model_lead
import control

def add_lead():
    name = input('nome: ')
    email = input('email: ')
    stage = input('etapa no funil de vendas: ')

    #validar os dados
    #depois de validado
    #precisamos modelar os dados do lead como um dict
    print(model_lead(name,email,stage))

    #agora... com meu lead modelado como dict
    #preciso enviar para o leads.json
    #para isso, vamos usar o control/controller
    control.create_lead(model_lead(name,email,stage))


    print('lead adicionado(func)')

def list_leads():
    leads = control.read_leads()
    print(leads)
    #+1 desafio: printar como tabela

def main():
    while True:
        print('\nmini CRM de leads')
        print('[1] adicionar lead')
        print('[2] listar lead')
        print('[3] sair do programa')

        opt = input('escolha uma opcao: ')

        if opt == '1':
            add_lead()
        elif opt == '2':
            list_leads()
        elif opt == '0':
            print('ate mais...')
            break
        else:
            print('opcao invalida')

if __name__ == '__main__':
    main()
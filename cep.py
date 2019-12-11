import requests
def qualCEP (cep):
    response = requests.get('https://viacep.com.br/ws/' + str(cep) + '/json' )
    infos = response.json()
    print ('CEP: ', infos['cep'])
    print ('COMP: ', infos['complemento'])
    print ('BAIRRO: ', infos['bairro'])
    print ('CIDADE: ', infos['localidade'])
    print ('UF: ', infos['uf'])
    #print(response.text)
    return infos
#print('Digite o CEP: ')
cepe = input('Digite o CEP: ')
qualCEP(cepe)
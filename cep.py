import requests
def qualCEP (cep):
    response = requests.get('https://viacep.com.br/ws/' + str(cep) + '/json' )
    infos = response.json()
    print(response.text)
    return infos
print('Digite o CEP: ')
cepe = input()
qualCEP(cepe)
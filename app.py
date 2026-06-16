#Requisição HTTP
import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' 

response = requests.get(url) #Nossa URL vira um endpoint, responsável por mostrar os dados apenas
print(response)

if response.status_code == 200:#status_code = 200 indica que a requisição foi um sucesso
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'], 
            "price": item['price'],
            "description": item['description']
    })
    
else:
    print(f"O erro de requisição foi {response.status_code}")

for nome_do_restaurante,dados in dados_restaurante.items(): #Pegando os 'items'
    nome_do_arquivo = f'{nome_do_restaurante}.json' #Avisando que nome_do_arquivo é = nome_do_restaurante.json 
    with open(nome_do_arquivo,'w') as arquivo_restaurantes: # Criando arquivo em branco.. usamos o w(= write), ou seja, vamos escrever nesses arquivos
        json.dump(dados,arquivo_restaurantes,indent=4) # dados são inseridos nos arquivos cirados acima
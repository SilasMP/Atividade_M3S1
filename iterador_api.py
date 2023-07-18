import requests
#classe que percorre sequencialmente entre os itens de um iteravel recebido como argumento. 
class Iterador:

    def __init__(self, iteravel):
        self.iteravel = iteravel
        self.max = len(iteravel)
        self.index = -1

    def __iter__(self):              
        return self
    
    def __next__(self):
         
        if self.index < (self.max-1):
            self.index +=1
            return self.iteravel[self.index]
        
        raise StopIteration()
    
#recebendo os dados tabela FIPE via API     
resposta = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas')
marcas_info = resposta.json() #armazenando os dados recebidos via json

marcas = Iterador(marcas_info) #primeiro uso do iterador para percorrer as informações de Marca e ID

for marca in marcas:
    print(f'Fabricante: {marca["nome"]} - ID: {marca["codigo"]}')

#Solicitando ao usuario o id da marca conforme informações disponiveis do print
id_marca_selecionada = int(input('Informe o numero do ID da Fabricante selecionada: '))

#nova consulta a API, agora para obter os modelos da marca via o numero do id informado via input
resposta = requests.get(f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{id_marca_selecionada}/modelos')
modelos_veiculos = resposta.json() #armazenando os dados recebidos via json
modelo_info = modelos_veiculos['modelos']

carros = Iterador(modelo_info) #segundo uso do iterador para percorrer as informações de Modelo e ID

for modelo in carros:
    print(f'Modelo: {modelo["nome"]} - ID: {modelo["codigo"]}')

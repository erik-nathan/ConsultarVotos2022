import pandas as pd
import json
import requests
# executar o <pip install -r requirements.txt> para instalar as dependencias

data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
json_data = json.loads(data.content)

candt = []
part = []
votos = []
porcent = []

for dados in json_data['cand']:
    if dados['seq'] in ['1', '2', '3', '4']:
        candt.append(dados['nm'])
        votos.append(dados['vap'])
        part.append(dados['cc'])
        porcent.append(dados['pvap'])

eleicao = pd.DataFrame(list(zip(candt, votos, part, porcent)), columns = ['   CANDIDATO', '   Nº VOTOS', '   PARTIDO', '   PORCENTAGEM'])

print(eleicao)
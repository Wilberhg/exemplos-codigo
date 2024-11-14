from queue import Queue  # Funcionalidade da fila
import requests  # Efetua requisições HTTP
import xml.etree.ElementTree as ET  # Permite analisar arquivos XMLs
import json  # Permite analisar arquivos JSON
from concurrent.futures import ThreadPoolExecutor  # Funcionalidade das Threads
import time

fila = Queue()

for moeda in ['USD', 'EUR', 'JPY', 'GBP', 'ARS']:
    fila.put(moeda)

print(fila.qsize())
# resultado: 5


def coleta_cotacao(moeda, datas):
    cotacoes = {moeda: []}  # Dicionario vazio para popular futuramente com as cotações
    siglas = {'USD': '220', 'EUR': '978',
              'JPY': '470', 'GBP': '540',
              'ARS': '706'}  # Dicionário contendo a sigla e qual o código da moeda
    for data in datas:  # Para cada data informada, fazer 1 interação
        retorno = requests.get(f'https://www3.bcb.gov.br/bc_moeda/rest/converter/1/1/{siglas[moeda]}/790/{data}')  # Faz requisição da cotação
        root = ET.fromstring(retorno.text)  # Converte o retorno XML em algo modificável pelo Python
        cotacoes[moeda].append({data: root.text})  # Adiciona data e o valor da cotação na chave contendo a sigla
    with open(f'cotacoes_{moeda}.json', 'w') as arqv:  # Salva um arquivo .json final
        json.dump(cotacoes, arqv)


tempo_inicial = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as executor:  # Gerenciador de contexto instanciado para executar as threads
    results = [executor.submit(coleta_cotacao,
               fila.get(),
               ['2024-02-09', '2024-02-08', '2024-02-07', '2024-02-06',
                '2024-02-05', '2024-02-02', '2024-02-01', '2024-01-31',
                '2024-01-30', '2024-01-29']) for _ in range(5)]  # List Comprehension interando uma "queue" com data padrões
tempo_final = time.perf_counter()
tempo_total = tempo_final - tempo_inicial
print(f"O tempo total da automação foi de {tempo_total:.2f} segundos")

from bs4 import BeautifulSoup
import requests
import json


def scrapping_producao(ano=2023):

    response = requests.get(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02')

    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')

        tabela = soup.find('table', attrs={'class': 'tb_base tb_dados'})
        tabela_body = tabela.find('tbody')
        linhas = tabela_body.find_all('tr')
        resultado = {} 


        nome_item = None

        for linha in linhas:
            td_item = linha.find_all('td', attrs={'class': 'tb_item'})
            
            if len(td_item) > 0:
                nome_item = td_item[0].text.strip()
                resultado[nome_item] = {}
                resultado[nome_item]['total'] = td_item[1].text.strip()
                resultado[nome_item]['itens'] = []
            else:
                td_subitem = linha.find_all('td', attrs={'class': 'tb_subitem'})
                if nome_item and len(td_subitem) > 0:
                    resultado[nome_item]['itens'].append({f'{td_subitem[0].text.strip()}': f'{td_subitem[1].text.strip()}'})
                   
    else:
        resultado = {'message': 'Nao foi possivel recuperar informacoes do site'}
    

    return resultado

def scrapping_comercializacao(ano=2023):

    response = requests.get(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_04')

    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')

        tabela = soup.find('table', attrs={'class': 'tb_base tb_dados'})
        tabela_body = tabela.find('tbody')
        linhas = tabela_body.find_all('tr')
        resultado = {} 


        nome_item = None

        for linha in linhas:
            td_item = linha.find_all('td', attrs={'class': 'tb_item'})
            
            if len(td_item) > 0:
                nome_item = td_item[0].text.strip()
                resultado[nome_item] = {}
                resultado[nome_item]['total'] = td_item[1].text.strip()
                resultado[nome_item]['itens'] = []
            else:
                td_subitem = linha.find_all('td', attrs={'class': 'tb_subitem'})
                if nome_item and len(td_subitem) > 0:
                    resultado[nome_item]['itens'].append({f'{td_subitem[0].text.strip()}': f'{td_subitem[1].text.strip()}'})
                   
    else:
        resultado = {'message': 'Nao foi possivel recuperar informacoes do site'}
    

    return resultado

def scrapping_processamento(ano=2023, opt=1):
   
    opcoes = {
        1: 'subopt_01',
        2: 'subopt_02',
        3: 'subopt_03',
        4: 'subopt_04'
    }

    response = requests.get(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_03&subopcao={opcoes[opt]}')

    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')

        tabela = soup.find('table', attrs={'class': 'tb_base tb_dados'})
        tabela_body = tabela.find('tbody')
        linhas = tabela_body.find_all('tr')
        resultado = {} 


        nome_item = None

        for linha in linhas:
            td_item = linha.find_all('td', attrs={'class': 'tb_item'})
            
            if len(td_item) > 0:
                nome_item = td_item[0].text.strip()
                resultado[nome_item] = {}
                resultado[nome_item]['total'] = td_item[1].text.strip()
                resultado[nome_item]['itens'] = []
            else:
                td_subitem = linha.find_all('td', attrs={'class': 'tb_subitem'})
                if nome_item and len(td_subitem) > 0:
                    resultado[nome_item]['itens'].append({f'{td_subitem[0].text.strip()}': f'{td_subitem[1].text.strip()}'})
                   
    else:
        resultado = {'message': 'Nao foi possivel recuperar informacoes do site'}
    

    return resultado

def scrapping_importacao(ano=2024, opt=1):

    opcoes = {
        1: 'subopt_01',
        2: 'subopt_02',
        3: 'subopt_03',
        4: 'subopt_04',
        5: 'subopt_05'
    }

    response = requests.get(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao={opcoes[opt]}')

    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')

        tabela = soup.find('table', attrs={'class': 'tb_base tb_dados'})
        tabela_body = tabela.find('tbody')
        linhas = tabela_body.find_all('tr')
        resultado = {} 

        for linha in linhas:
           campos = linha.find_all('td')
           nome_pais = campos[0].text.strip()
           quantidade = campos[1].text.strip()
           valor = campos[2].text.strip()
           resultado[nome_pais] = {}
           resultado[nome_pais]['Quantidade'] = quantidade
           resultado[nome_pais]['Valor'] = valor 
                   
    else:
        resultado = {'message': 'Nao foi possivel recuperar informacoes do site'}
    

    return resultado

def scrapping_exportacao(ano=2024, opt=1):

    opcoes = {
        1: 'subopt_01',
        2: 'subopt_02',
        3: 'subopt_03',
        4: 'subopt_04'
    }

    response = requests.get(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao={opcoes[opt]}')

    if(response.status_code == 200):
        soup = BeautifulSoup(response.text, 'html.parser')

        tabela = soup.find('table', attrs={'class': 'tb_base tb_dados'})
        tabela_body = tabela.find('tbody')
        linhas = tabela_body.find_all('tr')
        resultado = {} 


        if(response.status_code == 200):
            soup = BeautifulSoup(response.text, 'html.parser')

            tabela = soup.find('table', attrs={'class': 'tb_base tb_dados'})
            tabela_body = tabela.find('tbody')
            linhas = tabela_body.find_all('tr')
            resultado = {} 

            for linha in linhas:
                campos = linha.find_all('td')
                nome_pais = campos[0].text.strip()
                quantidade = campos[1].text.strip()
                valor = campos[2].text.strip()
                resultado[nome_pais] = {}
                resultado[nome_pais]['Quantidade'] = quantidade
                resultado[nome_pais]['Valor'] = valor 
                   
    else:
        resultado = {'message': 'Nao foi possivel recuperar informacoes do site'}
    

    return resultado
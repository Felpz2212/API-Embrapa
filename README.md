# 📊 API VitiBrasil Embrapa

Este projeto é uma API desenvolvida em Python que realiza web scraping no site oficial do [VitiBrasil Embrapa](http://vitibrasil.cnpuv.embrapa.br/index.php). A API coleta os dados disponíveis nas abas de **Produção**, **Processamento**, **Comercialização**, **Importação** e **Exportação**, convertendo as tabelas apresentadas no site para o formato JSON de forma estruturada e acessível.

## 🚀 Funcionalidades

- Scraping automático das tabelas de dados do site.
- Estruturação e retorno dos dados em formato JSON.
- Endpoints criados com Flask para facilitar o consumo dos dados.

## 🛠 Tecnologias utilizadas

- Python
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [Flask](https://flask.palletsprojects.com/)

## 📦 Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Felpz2212/API-Embrapa.git
   cd API-Embrapa
## 📦 Como rodar o projeto

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # no Windows: venv\Scripts\activate
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
4. **Execute a aplicação:**
   ```bash
   python app.py

5. **Acesse no navegador ou via ferramenta como Postman:**
http://localhost:5000/


📌 Observações
A estrutura e a disponibilidade dos dados dependem do site da Embrapa. Mudanças no HTML podem impactar o funcionamento do scraping.

Os dados retornados são atualizados conforme a estrutura apresentada nas páginas públicas do VitiBrasil.

## 🎯 Objetivos do projeto

Este projeto foi desenvolvido como parte de um desafio da **primeira fase da pós-graduação em Engenharia de Machine Learning da FIAP**. Os principais objetivos propostos foram:

- ✅ Criar uma **REST API em Python** que faça scraping de dados diretamente do site da **Embrapa (VitiBrasil)**.
- ✅ Documentar a API para facilitar sua utilização por outros desenvolvedores ou aplicações.
- ⚙️ (Opcional) Implementar um método de **autenticação** (como JWT) para segurança no acesso aos dados.
- 🧠 Planejar uma **arquitetura de deploy** da API, considerando um cenário em que ela possa alimentar um futuro modelo de machine learning.
- 🚀 Desenvolver um **MVP funcional**, realizar o **deploy com link acessível publicamente** e disponibilizar o código em um repositório no GitHub.

> 💡 A proposta também inclui a escolha de um **cenário realista e aplicável** para uso dos dados extraídos, com foco em sua utilidade futura para projetos de análise ou predição utilizando aprendizado de máquina.

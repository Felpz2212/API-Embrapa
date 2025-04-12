from flask import request, jsonify, Blueprint
from services.scrapper import scrapping_producao, scrapping_comercializacao, scrapping_processamento, scrapping_exportacao, scrapping_importacao

vitvini_bp = Blueprint('vitivini', __name__, url_prefix='/vitivini')

@vitvini_bp.route('/producao', methods=['GET'])
def get_producao():
    """
    Retorna dados de produção da vitivinicultura
    ---
    tags:
      - Produção
    parameters:
      - name: ano
        in: query
        type: integer
        required: false
        description: "Ano da produção (ex: 2023)"
    responses:
      200:
        description: "Dados de produção encontrados com sucesso"
        schema:
          type: object
    """
    ano = request.args.get('ano')
    if ano:
        return jsonify(scrapping_producao(ano))
    else:
        return jsonify(scrapping_producao())

@vitvini_bp.route('/comercializacao', methods=['GET'])
def get_comercializacao():
    """
    Retorna dados de comercialização de produtos vitivinícolas
    ---
    tags:
      - Comercialização
    parameters:
      - name: ano
        in: query
        type: integer
        required: false
        description: "Ano da comercialização (ex: 2023)"
    responses:
      200:
        description: "Dados de comercialização encontrados com sucesso"
        schema:
          type: object
    """
    ano = request.args.get('ano')
    if ano:
        return jsonify(scrapping_comercializacao(ano))
    else:
        return jsonify(scrapping_comercializacao())

@vitvini_bp.route('/processamento', methods=['GET'])
def get_processamento():
    """
    Retorna dados de processamento de uvas
    ---
    tags:
      - Processamento
    parameters:
      - name: ano
        in: query
        type: integer
        required: false
        description: "Ano do processamento (ex: 2023)"
      - name: opt
        in: query
        type: integer
        required: false
        enum: [1, 2, 3, 4]
        description: "Opção do tipo de dado a ser retornado. Valores possíveis:\n1 - Viniferas\n2 - Americanas e hibridas\n3 - Uvas de mesa\n4 - Sem classificacao"
    responses:
      200:
        description: "Dados de processamento encontrados com sucesso"
        schema:
          type: object
    """
    opt = request.args.get('opt')
    ano = request.args.get('ano')

    if ano and opt:
        return jsonify(scrapping_processamento(ano, int(opt)))
    elif ano:
        return jsonify(scrapping_processamento(ano))
    elif opt:
        return jsonify(scrapping_processamento(opt=int(opt)))
    else:
        return jsonify(scrapping_processamento())


@vitvini_bp.route('/exportacao', methods=['GET'])
def get_exportacao():
    """
    Retorna dados de exportação de produtos vitivinícolas
    ---
    tags:
      - Exportação
    parameters:
      - name: ano
        in: query
        type: integer
        required: false
        description: "Ano da exportação (ex: 2024)"
      - name: opt
        in: query
        type: integer
        required: false
        enum: [1, 2, 3, 4]
        description: "Opção do tipo de dado a ser retornado. Valores possíveis:\n1 - Vinhos de mesa\n2 - Espumantes\n3 - Uvas frescas\n4 - Suco de uva"
    responses:
      200:
        description: "Dados de exportação encontrados com sucesso"
        schema:
          type: object
    """
    opt = request.args.get('opt')
    ano = request.args.get('ano')

    if ano and opt:
        return jsonify(scrapping_exportacao(ano, int(opt)))
    elif ano:
        return jsonify(scrapping_exportacao(ano))
    elif opt:
        return jsonify(scrapping_exportacao(opt=int(opt)))
    else:
        return jsonify(scrapping_exportacao())


@vitvini_bp.route('/importacao', methods=['GET'])
def get_importacao():
    """
    Retorna dados de importação de produtos vitivinícolas
    ---
    tags:
      - Importação
    parameters:
      - name: ano
        in: query
        type: integer
        required: false
        description: "Ano da importação (ex: 2024)"
      - name: opt
        in: query
        type: integer
        required: false
        enum: [1, 2, 3, 4, 5]
        description: "Opção do tipo de dado a ser retornado. Valores possíveis:\n1 - Vinhos de mesa\n2 - Espumantes\n3 - Uvas frescas\n4 - Uvas passas\n5 - Suco de uva"
    responses:
      200:
        description: "Dados de importação encontrados com sucesso"
        schema:
          type: object
    """
    opt = request.args.get('opt')
    ano = request.args.get('ano')

    if ano and opt:
        return jsonify(scrapping_importacao(ano, int(opt)))
    elif ano:
        return jsonify(scrapping_importacao(ano))
    elif opt:
        return jsonify(scrapping_importacao(opt=int(opt)))
    else:
        return jsonify(scrapping_importacao())

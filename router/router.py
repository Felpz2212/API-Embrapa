from flask import request, jsonify, Blueprint
from services.scrapper import scrapping_producao, scrapping_comercializacao, scrapping_processamento, scrapping_exportacao, scrapping_importacao

vitvini_bp = Blueprint('vitivini', __name__, url_prefix='/vitivini')


@vitvini_bp.route('/producao', methods=['GET'])
def get_producao():
    ano = request.args.get('ano')
    if ano:
        return jsonify(scrapping_producao(ano))
    else:
        return jsonify(scrapping_producao())

@vitvini_bp.route('/comercializacao', methods=['GET'])
def get_comercializacao():
    ano = request.args.get('ano')
    if ano:
        return jsonify(scrapping_comercializacao(ano))
    else:
        return jsonify(scrapping_comercializacao())
    
@vitvini_bp.route('/processamento', methods=['GET'])
def get_processamento():
    opt = request.args.get('opt')
    ano = request.args.get('ano')
    
    if(ano and opt):
        return jsonify(scrapping_processamento(ano, int(opt)))
    elif(ano):
        return jsonify(scrapping_processamento(ano))
    elif(opt):
        return jsonify(scrapping_processamento(opt=int(opt)))
    else:
        return jsonify(scrapping_processamento())

@vitvini_bp.route('/exportacao', methods=['GET'])
def get_exportacao():
    opt = request.args.get('opt')
    ano = request.args.get('ano')
    
    if(ano and opt):
        return jsonify(scrapping_exportacao(ano, int(opt)))
    elif(ano):
        return jsonify(scrapping_exportacao(ano))
    elif(opt):
        return jsonify(scrapping_exportacao(opt=int(opt)))
    else:
        return jsonify(scrapping_exportacao())

@vitvini_bp.route('/importacao', methods=['GET'])
def get_importacao():
    opt = request.args.get('opt')
    ano = request.args.get('ano')
    
    if(ano and opt):
        return jsonify(scrapping_importacao(ano, int(opt)))
    elif(ano):
        return jsonify(scrapping_importacao(ano))
    elif(opt):
        return jsonify(scrapping_importacao(opt=int(opt)))
    else:
        return jsonify(scrapping_importacao())
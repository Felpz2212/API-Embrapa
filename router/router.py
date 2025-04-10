from flask import request, jsonify, Blueprint
from services.scrapper import scrapping_producao

vitvini_bp = Blueprint('vitivini', __name__, url_prefix='/vitivini')


@vitvini_bp.route('/producao', methods=['GET'])
def teste():
    ano = request.args.get('ano')
    if ano:
        return jsonify(scrapping_producao(ano))
    else:
        return jsonify(scrapping_producao())

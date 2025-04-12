from flask import Flask
from flasgger import Swagger
from router.router import vitvini_bp
import os

app = Flask(__name__)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger_template = {
    "info": {
        "title": "API Vitivinícola",
        "description": "Documentação da API de dados da produção, comercialização, processamento, exportação e importação vitivinícola.",
        "version": "1.0"
    },
    "basePath": "/vitivini", 
    "schemes": ["http"]
}

swagger = Swagger(app, template=swagger_template)

app.register_blueprint(vitvini_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)

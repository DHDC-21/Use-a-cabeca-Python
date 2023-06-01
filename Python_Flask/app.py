# Importações de bibliotecas
from flask import Flask, render_template
from src.controllers.routes.test_routes import test_bp
# from src.controllers.routes.main_routes import main_bp

# Configurando app
app = Flask(__name__,template_folder='./src\\views')

# Configurando as rotas
app.register_blueprint(test_bp)
'''
@app.route('/')
def index():
    return render_template('teste_index.html')
'''


# Iniciando app
app.run()
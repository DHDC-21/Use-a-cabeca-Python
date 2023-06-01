from flask import Blueprint, render_template


test_bp = Blueprint('test', __name__, url_prefix='/corno')


@test_bp.route('/')
def index():
    return render_template('teste_index.html',title='teste')

@test_bp.route('/teste2')
def teste2():
    return render_template('corno.html')

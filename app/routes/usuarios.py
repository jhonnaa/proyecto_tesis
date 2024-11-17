from . import bp

@bp.route('/usuarios')
def usuarios():
    return "Página de usuarios"

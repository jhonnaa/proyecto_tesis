from flask import flash, render_template , request,redirect, session
from . import bp
from app import bcrypt,db
from app.models import Admin, Medico , Persona, Paciente
# muestra todos los pacientes
@bp.route('/medicos', methods=["POST","GET"])
def medicosGetAllPaciente():
    if not session.get('admin_id'):
        return redirect('/admin/')
    if request.method== "POST":
        search=request.form.get('search')
        users = db.session.query(Persona, Medico).join(Medico, Persona.id == Medico.id_persona).filter(Persona.apellidos.like(f'%{search}%')).all()
        return render_template('medico/medicos.html',title='Approve Paciente',users=users)
    else:
        users = db.session.query(Persona, Medico).join(Medico, Persona.id == Medico.id_persona).all()
        return render_template('medico/medicos.html',title='Paciente',users=users)
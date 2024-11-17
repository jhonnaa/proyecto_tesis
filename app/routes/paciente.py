from flask import flash, render_template , request,redirect, session
from . import bp
from app import db
from app.models import Persona, Paciente,Historial

# Paciente Registro
@bp.route('/paciente/crear',methods=['POST','GET'])
def pacienteNuevo():
    if  session.get('user_id'):
        return redirect('/')
    if request.method=='POST':
        # get all input field name
        ci=request.form.get('ci')
        firstName=request.form.get('firstName')
        lastName=request.form.get('lastName')
        email=request.form.get('email')
        address=request.form.get('address')
        genero=request.form.get('genero')
        birthday=request.form.get('birthday')
        phone=request.form.get('phone')
        status=request.form.get('status')
        dateIn=request.form.get('dateIn')
        numberSafe=request.form.get('numberSafe')
        # check all the field is filled are not
        if ci =="" or firstName=="" or lastName=="" or email=="" or address=="" or genero=="" or birthday=="" or phone=="" or status=="":
            flash('Por favor complete los campos','danger')
            return redirect('/admin/paciente/crear')
        else:
            is_persona=Persona().query.filter_by(ci=ci).first()
            if is_persona:
                flash('el numero de CI esta registrada','danger')
                return redirect('/admin/paciente/crear')
            else:

                user=Persona(ci=ci,nombres=firstName,apellidos=lastName,email=email,direccion=address,genero=genero,fecha_nacimiento=birthday,telefono=phone,status=status)
                db.session.add(user)
                db.session.commit()
                paciente=Paciente(id_persona=user.id,numero_seguro=numberSafe,fecha_ingreso=dateIn)
                db.session.add(paciente)
                db.session.commit()
                flash('Account Create Successfully Admin Will approve your account in 10 to 30 mint ','success')
                return redirect('/admin/pacientes')
    else:
        return render_template('paciente/crear.html',title="Paciente Signup")
# profile paciente
@bp.route('/admin/paciente/<int:id>/editar')
def adminPaciente(id):
    if not session.get('admin_id'):
        return redirect('/admin/')
    paciente=Persona.query.get(id)
    return render_template('paciente/paciente.html',title="",id=id,paciente=paciente)

@bp.route('/admin/paciente/<int:id>/historiales')
def adminPacienteHistoriales(id):
    if not session.get('admin_id'):
        return redirect('/admin/')
    historiales=Historial.query.filter_by(id_paciente=id).all()
    return render_template('paciente/historiales.html',title="",id=id,historiales=historiales)

# previsualar
@bp.route('/admin/paciente/<int:id>/historial')
def adminPacientehistorial(id):
    if not session.get('admin_id'):
        return redirect('/admin/')
    historial=Historial.query.get(id)
    return render_template('paciente/historial.html',title="",historial=historial)

# diagnostico
@bp.route('/admin/paciente/<int:id>/diagnostico',methods=['POST','GET'])
def adminPacientediagnostico(id):
    if not session.get('admin_id'):
        return redirect('/admin/')
    if request.method=='POST':
        idPaciente=request.form.get('idPaciente')
        idMedico=request.form.get('idMedico')
        fecha=request.form.get('fecha')
        diagnostico=request.form.get('diagnostico')
        tratamiento=request.form.get('tratamiento')
        tipoArtrosis=request.form.get('tipoArtrosis')
        gradoSeveridad=request.form.get('gradoSeveridad')
        sintomas=request.form.get('sintomas')
        resultadosRadiologicos=request.form.get('resultadosRadiologicos')
        medicamentosRecetados=request.form.get('medicamentosRecetados')
        fisioterapia=request.form.get('fisioterapia')
        cirugiasPrevias=request.form.get('cirugiasPrevias')
        seguimiento=request.form.get('seguimiento')
        notas=request.form.get('notas')
        imagen=request.form.get('nameimage')
        if idPaciente =="" or idMedico=="" or fecha=="" or diagnostico=="" or tratamiento=="" or tipoArtrosis=="" or gradoSeveridad=="" or sintomas=="" or resultadosRadiologicos=="" or medicamentosRecetados=="" or fisioterapia=="" or cirugiasPrevias=="" or seguimiento=="" or notas=="" or imagen=="":
            flash('Por favor complete los campos','danger')
            return redirect('/admin/paciente/<int:id>/historiales')
        historial=Historial(id_paciente=idPaciente,id_medico=idMedico,fecha=fecha,diagnostico=diagnostico,tratamiento=tratamiento,tipo_artrosis=tipoArtrosis,grado_severidad=gradoSeveridad,sintomas=sintomas,resultados_radiologicos=resultadosRadiologicos,medicamentos_recetados=medicamentosRecetados,fisioterapia=fisioterapia,cirugias_previas=cirugiasPrevias,seguimiento=seguimiento,nota=notas,imagen=imagen)
        db.session.add(historial)
        db.session.commit()
        return redirect(f'/admin/paciente/{historial.id}/historial')
    return render_template('paciente/diagnostico.html',title="",id=id)
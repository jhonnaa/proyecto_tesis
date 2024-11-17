from flask import flash, render_template , request,redirect, session
from . import bp
from app import bcrypt,db
from app.models import Admin , Persona, Paciente

@bp.route('/')
def index():
    return render_template('index.html',title="")


# pagina de ingreso al sistema
@bp.route('/admin/',methods=["POST","GET"])
def adminIndex():
    # verifica si la petición es de tipo post
    if request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username=="" or password=="":
            flash('Complete los campos','danger')
            return redirect('/admin/')
        else:
            
            admins=Admin.query.filter_by(username=username).first()
            print(admins)
            if admins and bcrypt.check_password_hash(admins.password,password):
                session['admin_id']=admins.id
                session['admin_name']=admins.username
                session['tipo']=admins.tipo
                flash('Login Successfully','success')
                return redirect('/')
            else:
                flash('Invalid Email and Password','danger')
                return redirect('/admin/')
    else:
        return render_template('admin/index.html',title="Admin Login")

# muestra todos los pacientes
@bp.route('/admin/pacientes', methods=["POST","GET"])
def adminGetAllPaciente():
    if not session.get('admin_id'):
        return redirect('/admin/')
    if request.method== "POST":
        search=request.form.get('search')
        users = db.session.query(Persona, Paciente).join(Paciente, Persona.id == Paciente.id_persona).filter(Persona.apellidos.like(f'%{search}%')).all()
        return render_template('admin/pacientes.html',title='Approve Paciente',users=users)
    else:
        #users=Paciente.query.all()
        users = db.session.query(Persona, Paciente).join(Paciente, Persona.id == Paciente.id_persona).all()
        return render_template('admin/pacientes.html',title='Paciente',users=users)
    
# admin logout
@bp.route('/admin/logout')
def adminLogout():
    if not session.get('admin_id'):
        return redirect('/admin/')
    if session.get('admin_id'):
        session['admin_id']=None
        session['admin_name']=None
        return redirect('/')
    
# change admin password
@bp.route('/admin/change-admin-password',methods=["POST","GET"])
def adminChangePassword():
    admin=Admin.query.filter_by(username=session['admin_name']).first()
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if username == "" or password=="":
            flash('Please fill the field','danger')
            return redirect('/admin/change-admin-password')
        else:
            Admin().query.filter_by(username=username).update(dict(password=bcrypt.generate_password_hash(password,10)))
            db.session.commit()
            flash('Admin Password update successfully','success')
            return redirect('/admin/change-admin-password')
    else:
        return render_template('admin/admin-change-password.html',title='Admin Change Password',admin=admin)
    
@bp.route('/administradores', methods=["POST","GET"])
def administradoresGetAllPaciente():
    if not session.get('admin_id'):
        return redirect('/admin/')
    if request.method== "POST":
        search=request.form.get('search')
        users = db.session.query(Persona, Admin).join(Admin, Persona.id == Admin.id_persona).filter(Persona.apellidos.like(f'%{search}%')).all()
        return render_template('medico/medicos.html',title='Approve Paciente',users=users)
    else:
        users = db.session.query(Persona, Admin).join(Admin, Persona.id == Admin.id_persona).all()
        return render_template('admin/admin.html',title='Paciente',users=users)
# perfil admin
@bp.route('/admin/<int:id>/perfil',methods=['POST','GET'])
def adminPerfil(id):
    if not session.get('admin_id'):
        return redirect('/admin/')
    administrador=Persona.query.get(id)
    return render_template('admin/perfil.html',title="",id=id,administrador=administrador)
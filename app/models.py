from . import db

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ci = db.Column(db.Integer, default=0, nullable=False)
    nombres = db.Column(db.String(255), nullable=False)
    apellidos = db.Column(db.String(255), nullable=False)
    fecha_nacimiento = db.Column(db.String(255), nullable=False)
    genero = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return f'Persona("{self.id}","{self.ci}","{self.nombres}","{self.apellidos}","{self.fecha_nacimiento}","{self.genero}","{self.email}","{self.direccion}","{self.telefono}","{self.status}")'

#clase Paciente
class Paciente(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    id_persona=db.Column(db.Integer, nullable=False)
    numero_seguro=db.Column(db.String(255), nullable=False)
    fecha_ingreso=db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'Paciente("{self.id}","{self.id_persona}","{self.numero_seguro}","{self.fecha_ingreso}")'

# create admin Class
class Admin(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    id_persona=db.Column(db.Integer, nullable=False)
    username=db.Column(db.String(255), nullable=False)
    password=db.Column(db.String(255), nullable=False)
    tipo=db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'Admin("{self.username}","{self.id}","{self.id_persona}","{self.tipo}")'

#clase medico
class Medico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_persona = db.Column(db.Integer, nullable=False)
    especialidad = db.Column(db.String(255), nullable=False)
    numero_colegiado = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'Medico("{self.id}","{self.id_persona}","{self.especialidad}","{self.numero_colegiado}")'

#clase historial
class Historial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_paciente=db.Column(db.Integer, nullable=False)
    id_medico= db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.String(255), nullable=False)
    diagnostico=db.Column(db.String(255), nullable=False)
    tratamiento = db.Column(db.String(255), nullable=False)
    tipo_artrosis = db.Column(db.String(255), nullable=False)
    grado_severidad = db.Column(db.String(255), nullable=False)
    sintomas = db.Column(db.String(255), nullable=False)
    resultados_radiologicos = db.Column(db.String(255), nullable=False)
    medicamentos_recetados = db.Column(db.String(255), nullable=False)
    fisioterapia = db.Column(db.String(255), nullable=False)
    cirugias_previas = db.Column(db.String(255), nullable=False)
    seguimiento = db.Column(db.String(255), nullable=False)
    nota = db.Column(db.String(255), nullable=False)
    imagen = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'Historial("{self.id}","{self.id_paciente}","{self.id_medico}","{self.fecha}","{self.diagnostico}","{self.tratamiento}","{self.tipo_artrosis}","{self.grado_severidad}","{self.sintomas}","{self.resultados_radiologicos}","{self.medicamentos_recetados}","{self.fisioterapia}","{self.cirugias_previas}","{self.seguimiento}","{self.nota}")'
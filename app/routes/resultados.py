from datetime import datetime
from . import bp
import os
import cv2
import numpy as np
from flask import jsonify, request
import warnings
warnings.filterwarnings('ignore')

@bp.route("/predict", methods=["POST"])
def predict():

    image_data = request.files["file"].read()
    image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
    # Guardar una copia de la imagen antes de procesarla
    idpaciente = request.form['idpaciente']
    # Crear carpeta para idpaciente si no existe
    patient_folder = os.path.join('app/static/imagenes', idpaciente)
    if not os.path.exists(patient_folder):
        os.makedirs(patient_folder)
    # Generar un nuevo nombre de archivo usando la fecha y hora actuales
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    new_filename = f"{timestamp}_original.jpg"
    result_filename = f"{timestamp}_result.jpg"
    # Guardar archivo en la carpeta del paciente
    file_path = os.path.join(patient_folder, new_filename)
    file_path2 = os.path.join(patient_folder, result_filename)

    cv2.imwrite(file_path, image)
    cv2.imwrite(file_path2, image)



    return jsonify(idpaciente=idpaciente, timestamp=timestamp)
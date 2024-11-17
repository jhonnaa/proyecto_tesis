from flask import Blueprint

bp = Blueprint('main', __name__)

from .admin import *
from .resultados import *
from .paciente import *
from .medicos import *

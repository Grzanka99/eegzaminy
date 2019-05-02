from flask import Blueprint
from flask_restful import Api

api_v1 = Blueprint('v1', __name__)

from .exams import *
from .greeting import *
from .admin import *
from .access import *
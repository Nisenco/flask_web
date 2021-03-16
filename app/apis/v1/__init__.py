from flask import Blueprint
# flask_cors 解决前后端跨域问题
from flask_cors import CORS

api_v1 = Blueprint('api_v1', __name__)
CORS(api_v1)

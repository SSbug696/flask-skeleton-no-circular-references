from flask import Blueprint, render_template, jsonify

bp = Blueprint('base', __name__)

from ..models import *

@bp.route('/', methods=["GET"])
def home():
    row = Users(username='alex')
    db.session.add(row)
    db.session.commit()
    users = [{'username':r.username} for r in Users.query.all()]
    return jsonify(users)


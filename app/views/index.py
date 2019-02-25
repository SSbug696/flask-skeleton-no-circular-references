from flask import Blueprint, render_template, jsonify
bp = Blueprint('base', __name__)

from ..models import *

@bp.route('/', methods=["GET"])
def home():
    row = Users(username='alex')
    db.session.add(row)
    db.session.commit()
    Users.query.all()
    return render_template('index.html')

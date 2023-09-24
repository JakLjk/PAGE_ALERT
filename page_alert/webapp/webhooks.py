import json
from flask import Blueprint, request, jsonify
from .models import UserProcess
from flask_login import current_user
from . import db

webhooks = Blueprint('webhooks', __name__)

@webhooks.route("/delete_alert", methods=['POST'])
def return_alert_details():
    alert_data = json.loads(request.data)
    alert_id = alert_data['alert_id']
    alert = UserProcess.query.get(alert_id)
    print('delete')
    if alert:
        if alert.user_id == current_user.id:
            db.session.delete(alert)
            db.session.commit()
            return jsonify({})



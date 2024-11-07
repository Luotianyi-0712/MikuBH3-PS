import json
from flask import Blueprint, request, jsonify
from sdk_server.models.risky_check import RiskyCheck,DataScheme
from sdk_server.models.granter_login_body import GranterLoginBody

account_blueprint = Blueprint('account', __name__)

@account_blueprint.route('/account/risky/api/check', methods=['POST'])
def check_risky():
    return jsonify({
        "retcode":0,
        "message":"",
        "data":{
            "id":"",
            "action":"ACTION_NONE",
            "geetest":None
        }
    })

@account_blueprint.route('/<game_biz>/combo/granter/login/v2/login', methods=['POST'])
def granter_login(game_biz):
    body = request.json
    granter_login_body = GranterLoginBody(**body)

    granter_login_body_data = json.loads(granter_login_body.data)

    return jsonify({
        "retcode": 0,
        "message": "OK",
        "data": {
            "combo_id": "0",
            "open_id": granter_login_body_data['uid'],
            "combo_token": granter_login_body_data['token'],
            "data": {"guest": granter_login_body_data['guest']},
            "heartbeat": False,
            "account_type": 1
        }
    })

@account_blueprint.route('/<game_biz>/mdk/shield/api/verify', methods=['POST'])
def verify_shield(game_biz):
    shield_login_response = {
        "retcode": 0,
        "message": "OK",
        "data": {
            "account": {
                "uid": "1337",
                "name": "Miku",
                "email": "",
                "mobile": "",
                "is_email_verify": "0",
                "realname": "",
                "identity_card": "",
                "token": "12931313131",
                "safe_mobile": "",
                "facebook_name": "",
                "google_name": "",
                "twitter_name": "",
                "game_center_name": "",
                "apple_name": "",
                "sony_name": "",
                "tap_name": "",
                "country": "SG",
                "reactivate_ticket": "",
                "area_code": "**",
                "device_grant_ticket": "",
                "steam_name": "",
                "unmasked_email": "",
                "unmasked_email_type": 0
            },
            "device_grant_required": False,
            "safe_mobile_required": False,
            "realperson_required": False,
            "reactivate_required": False,
            "realname_operation": "None"
        }
    }

    return jsonify(shield_login_response)

@account_blueprint.route('/<game_biz>/mdk/shield/api/login', methods=['POST'])
def shield_login(game_biz):

    shield_login_response = {
        "retcode": 0,
        "message": "OK",
        "data": {
            "account": {
                "uid": "1337",
                "name": "Miku",
                "email": "",
                "mobile": "",
                "is_email_verify": "0",
                "realname": "",
                "identity_card": "",
                "token": "12931313131",
                "safe_mobile": "",
                "facebook_name": "",
                "google_name": "",
                "twitter_name": "",
                "game_center_name": "",
                "apple_name": "",
                "sony_name": "",
                "tap_name": "",
                "country": "SG",
                "reactivate_ticket": "",
                "area_code": "**",
                "device_grant_ticket": "",
                "steam_name": "",
                "unmasked_email": "",
                "unmasked_email_type": 0
            },
            "device_grant_required": False,
            "safe_mobile_required": False,
            "realperson_required": False,
            "reactivate_required": False,
            "realname_operation": "None"
        }
    }
    
    return jsonify(shield_login_response)

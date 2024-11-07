from flask import Blueprint, jsonify, request
import random
from datetime import datetime, timedelta


config_blueprint = Blueprint('config', __name__)

@config_blueprint.route('/<game_biz>/mdk/agreement/api/getAgreementInfos', methods=['GET'])
def get_agreement_infos(game_biz):
    return jsonify({
        "retcode": 0,
        "message": "OK",
        "data": {
            "marketing_agreements": []
        }
    })

@config_blueprint.route('/data_abtest_api/config/experiment/list', methods=['POST'])
def get_experiment_list():
    return jsonify({
        "retcode": 0,
        "success": True,
        "message": "",
        "data": []
    })

@config_blueprint.route('/account/device/api/listNewerDevices', methods=['POST'])
def list_newer_devices():
    return jsonify({
        "data": {
            "devices": [],
            "latest_id": "0"
        },
        "message": "OK",
        "retcode": 0
    })

@config_blueprint.route('/<game_biz>/combo/granter/api/getConfig', methods=['GET'])
def get_config(game_biz):
    return jsonify({
        "retcode": 0,
        "message": "OK",
        "data": {
            "protocol": True,
            "qr_enabled": False,
            "log_level": "DEBUG",
            "announce_url": f"https://127.0.0.1/bh3/announcement/",
            "push_alias_type": 2,
            "disable_ysdk_guard": False,
            "enable_announce_pic_popup": False,
            "app_name": "崩坏3-东南亚",
            "qr_enabled_apps": {
                "bbs": False,
                "cloud": False
            },
            "qr_app_icons": {
                "app": "",
                "bbs": "",
                "cloud": ""
            },
            "qr_cloud_display_name": ""
        }
    })

@config_blueprint.route('/game_weather/weather/get_weather', methods=['GET'])
def get_weather():
    weather_data = {
        "Retcode": 0,
        "Message": "OK",
        "Data": {
            "Timezone": 8,
            "Hourly": []
        }
    }
    for i in range(24):
        date_time = (datetime.now() + timedelta(hours=i)).strftime("%Y-%m-%d %H")
        weather_data["Data"]["Hourly"].append({
            "Condition": 1,
            "Date": date_time.split()[0],
            "Hour": int(date_time.split()[1].split(':')[0]),
            "Temp": random.randint(20, 30)
        })
    return jsonify(weather_data)

@config_blueprint.route('/<game_biz>/mdk/shield/api/loadConfig', methods=['GET'])
def load_config(game_biz):
    game_key = request.args.get('game_key', '')
    return jsonify({
        "retcode": 0,
        "message": "OK",
        "data": {
            "id": 16,
            "game_key": game_key,
            "client": "PC",
            "identity": "I_IDENTITY",
            "guest": False,
            "ignore_versions": "",
            "scene": "S_NORMAL",
            "name": "崩坏3rd-东南亚",
            "disable_regist": False,
            "enable_email_captcha": False,
            "thirdparty": [],
            "disable_mmt": False,
            "server_guest": False,
            "thirdparty_ignore": {},
            "enable_ps_bind_account": False,
            "thirdparty_login_configs": {},
            "initialize_firebase": False
        }
    })

@config_blueprint.route('/combo/box/api/config/sdk/combo', methods=['GET'])
def sdk_combo():
    return jsonify({
        "retcode": 0,
        "message": "OK",
        "data": {
            "vals": {
                "list_price_tierv2_enable": "false",
                "network_report_config": {
                    "enable": 0,
                    "status_codes": [206],
                    "url_paths": ["dataUpload", "red_dot"]
                },
                "kibana_pc_config": {
                    "enable": 1,
                    "level": "Debug",
                    "modules": ["download"]
                }
            }
        }
    })

@config_blueprint.route('/device-fp/api/getExtList', methods=['GET'])
def get_ext_list():
    return jsonify({
        "retcode": 0,
        "message": "OK",
        "data": {
            "code": 200,
            "msg": "ok",
            "ext_list": [
                "cpuName", "deviceModel", "deviceName", "deviceType", "deviceUID", "gpuID", "gpuName", "gpuAPI",
                "gpuVendor", "gpuVersion", "gpuMemory", "osVersion", "cpuCores", "cpuFrequency", "gpuVendorID",
                "isGpuMultiTread", "memorySize", "screenSize", "engineName", "addressMAC"
            ],
            "pkg_list": [],
            "pkg_str": "/vK5WTh5SS3SAj8Zm0qPWg=="
        }
    })

@config_blueprint.route('/device-fp/api/getFp', methods=['GET'])
def get_fp():
    device_fp = request.args.get('device_fp', '')
    return jsonify({
        "data": {
            "code": 200,
            "device_fp": device_fp,
            "msg": "ok"
        },
        "message": "OK",
        "retcode": 0
    })

@config_blueprint.route('/report', methods=['GET'])
def report():
    return "GET LOG"

@config_blueprint.route('/admin/mi18n/<path:remainder>', methods=['GET'])
def admin_mi18n(remainder):
    return jsonify({
        "version": 74
    })

@config_blueprint.route('/sdk/dataUpload', methods=['GET'])
def data_upload():
    return jsonify({
        "code": 0
    })

@config_blueprint.route('/<game_biz>/combo/granter/api/compareProtocolVersion', methods=['POST'])
def compare_protocol_version(game_biz):
    body = request.json
    app_id = body.get('AppId')
    language = body.get('Language')
    return jsonify({
        "retcode": 0,
        "message": "OK",
        "data": {
            "modified": True,
            "protocol": {
                "id": 0,
                "app_id": app_id,
                "language": language,
                "user_proto": "",
                "priv_proto": "",
                "major": 0,
                "minimum": 3,
                "create_time": "0",
                "teenager_proto": "",
                "third_proto": ""
            }
        }
    })

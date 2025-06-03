from flask import Blueprint, request, jsonify
from utils import fetch_weather_data
from gcs_helper import upload_to_gcs, list_files, download_from_gcs
import datetime

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/store-weather-data', methods=['POST'])
def store_weather_data():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    if not all([latitude, longitude, start_date, end_date]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        weather_json = fetch_weather_data(latitude, longitude, start_date, end_date)
        file_name = f"weather_{latitude}_{longitude}_{start_date}_to_{end_date}.json"
        upload_to_gcs(file_name, weather_json)
        return jsonify({"message": "Weather data stored successfully", "file_name": file_name}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@weather_bp.route('/list-weather-files', methods=['GET'])
def list_weather_files():
    try:
        files = list_files()
        return jsonify({"files": files}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@weather_bp.route('/weather-file-content/<file_name>', methods=['GET'])
def get_weather_file(file_name):
    try:
        content = download_from_gcs(file_name)
        return jsonify(content), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

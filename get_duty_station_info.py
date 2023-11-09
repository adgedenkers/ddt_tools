'''
File: get_duty_station_info.py
Project: ddt_tools
Created Date: 2023-11-02
Author: Adge Denkers
Email: adriaan.denkers@va.gov
-----
Last Modified: 2023-11-02
Modified By: Adge Denkers
Email: adriaan.denkers@va.gov
-----
Copyright (c) 2023 U.S. Department of Veterans Affairs
-----
NOTICE:
This code/script is the explicit property of the United States Government
which may be used only for official Governemnt business by authorized
personnel. Unauthorized access or use of this code/script may subject 
violators to criminal, civil, and/or administrative action.
'''
from flask import Flask, jsonify, request
from flask_caching import Cache
import requests
import time

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})
CACHE_TIMEOUT = 300  # Cache data for 5 minutes

STATIONS_URL = 'https://vaww.va.gov/HRIS/apps/hrissync/STATIONS.TXT'

@app.route('/station', methods=['GET'])
@cache.cached(timeout=CACHE_TIMEOUT, query_string=True)

def get_station():
    station_code = request.args.get('code', '')
    stations_data = fetch_and_parse_data()
    station = next((s for s in stations_data if station_code == s['station_code']), None)
    if station:
        return jsonify(station)
    return jsonify({'error': 'Station not found'}), 404

def fetch_and_parse_data():
    # Check if the data is already cached
    cached_data = cache.get('stations_data')
    if cached_data:
        return cached_data

    # If not cached, fetch new data
    response = requests.get(STATIONS_URL, verify=False)
    lines = response.text.splitlines()
    stations_data = [parse_line(line) for line in lines[7:]]
    cache.set('stations_data', stations_data, timeout=CACHE_TIMEOUT)
    return stations_data

def parse_line(line):
    return {
        'station_number': line[0:8].strip(),
        'station_code': line[8:16].strip(),
        # ... other fields ...
    }

if __name__ == '__main__':
    app.run(debug=True, port=88)
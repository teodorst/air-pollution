from flask import Flask, jsonify, request, json, Response, send_from_directory
import urllib2
import random
import sys
import re
import os
from flask_cors import CORS, cross_origin
import json
from flask_cache import Cache


from managers.resources_manager import Resources_Manager
from managers.statistics_manager import Statistics_Manager


def _read_romania_data_file():
    ro_data = None
    with open('romania.geojson', 'r') as romania_data_file:
        ro_data = romania_data_file.read()

    return ro_data


if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app)
    cache = Cache(app,config={'CACHE_TYPE': 'simple'})

    statistics_manager = Statistics_Manager()
    resources_manager = Resources_Manager()

    @app.route('/api/ro_map_data')
    @cache.cached(timeout=2592000)
    def get_romania_map_data():
        response = {
            'coords': _read_romania_data_file(),
            'center': [45.970, 25.203]
        }

        response = jsonify(response)
        response.status_code = 200

        return response

    @app.route('/api/counties')
    @cache.cached(timeout=2592000)
    def get_counties():
        counties = resources_manager.get_counties()
        response = {
            'counties': counties,
            'counties_number': len(counties)
        }
        response = jsonify(response)
        response.status_code = 200

        return response

    app.run(threaded=True, host='0.0.0.0', port='8000', )


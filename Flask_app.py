from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/collegevorming', methods=['GET'])
def collegevorming():
        try:
                with open('gm_data.json', 'r') as json_in:
                        data = json.load(json_in)
        except:
                return 'Error parsing data'

        if 'gm_naam' in request.args:
                gm_naam = request.args['gm_naam']
        else:
                return "Error: no gm_naam supplied"

        if gm_naam in data:
                return jsonify(data[gm_naam])
        else:
                return f"No data for {gm_naam} in database"

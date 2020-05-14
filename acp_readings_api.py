from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
from os import listdir, path
import json
from collections import defaultdict
import sys
from datetime import datetime
from pathlib import Path

app = Flask(__name__)

cors = CORS(app)

basePath = Path(__file__).resolve().parent.parent.joinpath('ttndata','media','acp')
DEBUG = True

def date_to_path(selecteddate):
    data = selecteddate.split('-')
    return(data[0]+'/'+data[1]+'/'+data[2]+'/')

def getDateToday():
    dt = datetime.now()
    return dt.strftime("%Y-%m-%d")
    

@app.route('/api/historicaldata')
def history_data():
    if DEBUG:
        print('Requested')

    sensor = "ijl20-sodaq-ttn"
    feature = "temperature"
    workingDir = ''
    rdict = defaultdict(float)
    print(request)
    try:
        selecteddate = request.args.get('date')
        source = request.args.get('source')
        sensor = request.args.get('sensor')
        feature = request.args.get('feature')
        workingDir = Path(basePath).resolve().joinpath(source,'data_bin',date_to_path(selecteddate))
        # workingDir = basePath+source+'/data_bin/'+date_to_path(selecteddate)
        if not path.exists(workingDir):
            sensor = "ijl20-sodaq-ttn"
            feature = "temperature"
            selecteddate = getDateToday()
            workingDir = Path(basePath).resolve().joinpath('mqtt_ttn','data_bin',date_to_path(selecteddate))
            # workingDir = basePath+'mqtt_ttn/data_bin/'+date_to_path(selecteddate)
    except:
        if DEBUG:
            print(sys.exc_info())
            print(request.args)
        sensor = "ijl20-sodaq-ttn"
        feature = "temperature"
        selecteddate = getDateToday()
        workingDir = Path(basePath).resolve().joinpath('mqtt_ttn','data_bin',date_to_path(selecteddate))
        # workingDir = basePath+'mqtt_ttn/data_bin/'+date_to_path(selecteddate)
    response = {}
    response['data'] = []

    for f in listdir(workingDir):
        fpath = Path(workingDir).resolve().joinpath(f)
        with open(fpath) as json_file:
            data = json.load(json_file)
            if data['dev_id'] == sensor:
                try:
                    rdict[float(f.split('_')[0])] = data['payload_fields'][feature]
                except KeyError:
                    pass
    
    for k in sorted(rdict.keys()):
        response['data'].append({'ts':str(k), 'val':rdict[k]})
    response['date'] = selecteddate
    response['sensor'] = sensor
    response['feature'] = feature

    json_response = json.dumps(response)
    return(json_response)

app.run(port=8001,debug=DEBUG)
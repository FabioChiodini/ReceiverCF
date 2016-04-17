from flask import Flask, request, jsonify
from pprint import pprint
import json

app = Flask(__name__)

#Added this k
#port=os.environ['PORTK']

@app.route('/log', methods=['POST'])
def log():
    try:
        data_to_log = json.loads(request.json)
        pprint(data_to_log)
    except Exception as e:
        print(e)
        raise(e)
    return(jsonify({'result':'ok'}))

#added for display
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def honey(path):
    log_request(request)
    return jsonify({'result': 'Receiver ok'})
#added for display end

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080, debug=True)

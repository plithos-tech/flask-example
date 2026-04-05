import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'message': 'Hey I am running now. The app is working.',
        'status': 'ok'
    })

@app.route('/env')
def dump_env():
    # Dump all environment variables
    env_vars = dict(os.environ)
    return jsonify({
        'environment': env_vars
    })

@app.route('/env/<key>')
def get_env(key):
    # Get a specific environment variable
    value = os.environ.get(key)
    if value is None:
        return jsonify({
            'error': f'Environment variable {key} not found'
        }), 404
    return jsonify({
        'key': key,
        'value': value
    })

application = app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
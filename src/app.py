"""
endpoint for calculation script
"""

from flask import Flask, request, jsonify
from scripts.math_expression import evaluate_expression
from main import main as execute_main_script

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    calculate expressions
    """
    data = request.get_json()
    expression = data.get('expression')
    if not expression:
        return jsonify({'error': 'No expression provided'}), 400

    try:
        result = evaluate_expression(expression)
        execute_main_script()

        return jsonify({'result': result, 'message': 'Script executed successfully'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import Flask, request, jsonify
from flask.cli import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Your personal information
USER_ID = os.getenv("USER_ID", "sonu_kumar_13072003")
EMAIL = os.getenv("EMAIL", "sonu.kumar2021@vitstudent.ac.in")
ROLL_NUMBER = os.getenv("ROLL_NUMBER", "21BCT0220")

@app.route('/api/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    
    if not data:
        return jsonify({"is_success": False, "error": "No data provided"}), 400
    
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_lowercase = max((char for char in alphabets if char.islower()), default=None)
    
    response = {
        "is_success": True,
        "user_id": USER_ID,
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
    }
    
    return jsonify(response)

@app.route('/api/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

# For local testing
if __name__ == '__main__':
    app.run(debug=True)
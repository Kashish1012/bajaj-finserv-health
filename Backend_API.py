from flask import Flask, request, jsonify

app = Flask(_name_)

# Hardcoded values
user_id = "john_doe_17091999"
email = "john@xyz.com"
roll_number = "ABCD123"

@app.route('/bfhl', methods=['POST'])
def post_request():
    try:
        data = request.get_json()['data']
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        highest_lowercase_alphabet = [max([x for x in alphabets if x.islower()], default='')]

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)})

@app.route('/bfhl', methods=['GET'])
def get_request():
    return jsonify({"operation_code": 1})

if _name_ == '_main_':
    app.run(debug=True)from flask import Flask, request, jsonify

app = Flask(_name_)

# Hardcoded values
user_id = "john_doe_17091999"
email = "john@xyz.com"
roll_number = "ABCD123"

@app.route('/bfhl', methods=['POST'])
def post_request():
    try:
        data = request.get_json()['data']
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        highest_lowercase_alphabet = [max([x for x in alphabets if x.islower()], default='')]

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)})

@app.route('/bfhl', methods=['GET'])
def get_request():
    return jsonify({"operation_code": 1})

if _name_ == '_main_':
    app.run(debug=True)from flask import Flask, request, jsonify

app = Flask(_name_)

# Hardcoded values
user_id = "john_doe_17091999"
email = "john@xyz.com"
roll_number = "ABCD123"

@app.route('/bfhl', methods=['POST'])
def post_request():
    try:
        data = request.get_json()['data']
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        highest_lowercase_alphabet = [max([x for x in alphabets if x.islower()], default='')]

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)})

@app.route('/bfhl', methods=['GET'])
def get_request():
    return jsonify({"operation_code": 1})

if _name_ == '_main_':
    app.run(debug=True)
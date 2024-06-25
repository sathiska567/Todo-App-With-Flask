from flask import request, jsonify
from app import app
from db import db
import bcrypt

# register users
@app.route('/register', methods=['POST'])
def register_data():
    try:
        user = request.get_json()
        print(user)
        
        if not user or 'name' not in user or 'email' not in user or 'password' not in user:
            return jsonify({
                "error": "Invalid request"
            }), 400
        
        # Encode the password to bytes before hashing
        password_bytes = user['password'].encode('utf-8')
        
        # Hash the password
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        
        # Store the hashed password
        user['password'] = hashed_password
        
        # Check if user already exists
        existing_user = db.register_details.find_one({'email': user['email']})
        if existing_user:
            return jsonify({
                "error": "User already exists"
            }), 400
        
        db_response = db.register_details.insert_one(user)
        print(db_response)
        
        return jsonify({
            "message": "User registered successfully"
        }), 201
    except Exception as e:
        print(e)
        return jsonify({
            "error": str(e)
        }), 500


# login users
@app.route('/login', methods=['GET','POST'])
def login_data():
    try:
        user = request.get_json()
        email = user['email']
        password = user['password']
        print(user)
        
        if not user or 'email' not in user or 'password' not in user:
            return jsonify({
                "error": "Invalid request"
            }), 400
        
        # Check if user exists
        existing_user = db.register_details.find_one({'email': email})
        if not existing_user:
            return jsonify({
                "error": "User not found"
            }), 404
        
        # Check password
        check_password = bcrypt.checkpw(password.encode('utf-8'), existing_user['password'])
        
        if not check_password:
            return jsonify({
                "error": "Invalid credentials"
            }), 401
        
        # Convert ObjectId to string
        # existing_user['_id'] = str(existing_user['_id'])
        
        return jsonify({
            "message": "Login successful",
            "user": str(existing_user['_id'])
        }), 200
                    
    except Exception as ex:
        print(ex)
        return jsonify({
            "error": str(ex)
        }), 500
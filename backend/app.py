from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import requests

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mental_wellness.db'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        token = create_access_token(identity=user.id)
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/journal', methods=['POST'])
@jwt_required()
def add_journal_entry():
    user_id = get_jwt_identity()
    data = request.get_json()
    entry = JournalEntry(content=data['content'], user_id=user_id)
    db.session.add(entry)
    db.session.commit()
    return jsonify({'message': 'Journal entry added'}), 201

@app.route('/journal', methods=['GET'])
@jwt_required()
def get_journal_entries():
    user_id = get_jwt_identity()
    entries = JournalEntry.query.filter_by(user_id=user_id).all()
    return jsonify({'entries': [{'id': entry.id, 'content': entry.content} for entry in entries]}), 200

@app.route('/journal/<int:entry_id>', methods=['PUT'])
@jwt_required()
def update_journal_entry(entry_id):
    user_id = get_jwt_identity()
    entry = JournalEntry.query.filter_by(id=entry_id, user_id=user_id).first()
    if not entry:
        return jsonify({'message': 'Journal entry not found'}), 404
    data = request.get_json()
    entry.content = data['content']
    db.session.commit()
    return jsonify({'message': 'Journal entry updated'}), 200

@app.route('/journal/<int:entry_id>', methods=['DELETE'])
@jwt_required()
def delete_journal_entry(entry_id):
    user_id = get_jwt_identity()
    entry = JournalEntry.query.filter_by(id=entry_id, user_id=user_id).first()
    if not entry:
        return jsonify({'message': 'Journal entry not found'}), 404
    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message': 'Journal entry deleted'}), 200

@app.route('/chatbot', methods=['POST'])
def chat_with_bot():
    data = request.get_json()
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={'Authorization': 'Bearer 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'},
        json={
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': data['message']}]
        }
    )
    if response.ok:


        return jsonify(response.json()), 200
    else:
        return jsonify({'message': 'Error communicating with ChatGPT API'}), response.status_code

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
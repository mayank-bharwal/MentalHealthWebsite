from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify,session
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mindscape.db'
app.secret_key = 'your_secret_key'  # Replace 'your_secret_key' with a real secret key

db = SQLAlchemy(app)

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    entry = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    recommendation = db.Column(db.String(500), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/test')
def test():
    # Make sure the user is logged in to take the test
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('test.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user is None:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            return 'User already exists.'
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password.'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))
# ... existing code ...

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    # Fetch journal entries for the logged-in user
    journal_entries = Journal.query.filter_by(user_id=session['user_id']).order_by(Journal.created_at.desc()).all()
    return render_template('dashboard.html', journal_entries=journal_entries)

# ... existing code ...

@app.route('/submit-test', methods=['POST'])
def submit_test():
    if 'user_id' not in session:
        return jsonify({'message': 'User not logged in'}), 401
    
    data = request.get_json()
    # Store the test result in the session for immediate access on the dashboard
    session['last_test_result'] = {'score': data['score'], 'recommendation': data['recommendation']}
    
    # You can also save the result to the database as before
    new_result = TestResult(user_id=session['user_id'], score=data['score'], recommendation=data['recommendation'])
    db.session.add(new_result)
    db.session.commit()

    return jsonify({'message': 'Test result saved'}), 200

@app.route('/submit_journal_entry', methods=['POST'])
def submit_journal_entry():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    entry = request.form['journal_entry']
    new_entry = Journal(user_id=session['user_id'], entry=entry)
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('dashboard'))
@app.route('/journal')
def journal():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    journal_entries = Journal.query.filter_by(user_id=session['user_id']).order_by(Journal.created_at.desc()).all()
    return render_template('journal.html', journal_entries=journal_entries)


# Add other routes and logic as needed ...

if __name__ == '__main__':
    app.run(debug=True)

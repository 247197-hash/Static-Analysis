from flask import Flask, request

app = Flask(__name__)

# ISSUE 1: Hardcoded Password (Security Risk)
DB_PASSWORD = "my-secret-password-123"

@app.route('/')
def home():
    # ISSUE 2: Simple Greeting
    return "<h1>Hello! This is my Lab 10 App</h1>"

@app.route('/search')
def search():
    # ISSUE 3: Potential XSS (Dynamic tool will catch this)
    user_input = request.args.get('q', '')
    return f"You searched for: {user_input}"

if __name__ == '__main__':
    # ISSUE 4: Debug Mode ON (Risk for ZAP scan)
    app.run(debug=True, port=5000)

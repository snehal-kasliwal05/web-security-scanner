from flask import Flask, request
from markupsafe import Markup

app = Flask(__name__)

# VULNERABLE: Using Markup (disables auto-escaping)
@app.route('/vulnerable/')
def vulnerable():
    user_input = request.args.get('name', 'Guest')
    html = Markup(f"<h1>Hello {user_input}</h1>")  # DANGEROUS!
    return html

# SAFE: Auto-escaping works
@app.route('/safe/')
def safe():
    user_input = request.args.get('name', 'Guest')
    return f"<h1>Hello {user_input}</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)

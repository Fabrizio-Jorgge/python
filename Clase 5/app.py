from flask import Flask
from login import login
from logout import logout

app = Flask(__name__)

app.register_blueprint(login)
app.register_blueprint(logout)
@app.route('/', methods=['GET'])
def home():
    return "Server Flask is running on port 5000"
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
